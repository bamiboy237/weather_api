from flask import Flask, render_template, flash, redirect, url_for, jsonify
from config import Config
from app.forms import WeatherForm
import requests
import json, os
import redis
from datetime import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import google.generativeai as genai



# Initialize Flask application
app = Flask(__name__)


# Initialize Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Initialize rate limiter
limiter = Limiter(get_remote_address)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def index():
    form = WeatherForm()
    if form.validate_on_submit():
        city = form.cityname.data
        # Construct the API URL for fetching weather data
        base_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&include=current%2Cevents%2Calerts&key={os.environ.get('WEATHER_API_KEY')}&contentType=json'
        
        try:
            # Fetch weather data from the API
            response = requests.get(base_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            weather_data = response.json()  # Parse the JSON response
            
            # Store the weather data in Redis
            redis_client.set('weather_data', json.dumps(weather_data))
            flash(f'Weather data for {city} successfully captured', 'success')
            return redirect('/weather')
        except requests.exceptions.RequestException as e:
            # Handle request errors
            flash(f'Error fetching weather data: {str(e)}', 'error')
            return redirect('/index')
        except json.JSONDecodeError:
            # Handle JSON parsing errors
            flash('Error parsing weather data. Please try again.', 'error')
            return redirect('/index')
        except Exception as e:
            # Handle any other exceptions
            flash(f'An unexpected error occurred: {str(e)}', 'error')
            return redirect('/index')

    return render_template('index.html', title='home', form=form)


@app.route('/weather', methods=['POST', 'GET'])
def weather():
    # Retrieve weather data from Redis
    weather_json = redis_client.get('weather_data')
    
    if weather_json:
        weather_data = json.loads(weather_json)
    else:
        flash('No weather data available. Please fetch it first.', 'error')
        return redirect('/index')  # Redirect if no data is available

    # Extract weather information
    try:        
        date = datetime.strptime(weather_data['days'][0]["datetime"], "%Y-%m-%d").strftime("%A")
        avg_temp = weather_data['days'][0]['temp']
        max_temp = weather_data['days'][0]['tempmax']
        min_temp = weather_data['days'][0]['tempmin']
        description = weather_data['days'][0]['description']
        city = weather_data['resolvedAddress'].title()
        wind_speed = weather_data['days'][0]['windspeed']
        humidity = weather_data['days'][0]['humidity']
        pressure = weather_data['days'][0]['pressure']
        dew = weather_data['days'][0]['dew']

        ## Use google genai for weather summary
        genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"You are a professional news reporter analyze the weather data in {weather_json} and produce a VERY short concise report of the , include suggestion and cautions. A one line short summary of the weather and a one line short suggestion on activities or what to wear and/or a caution")
        summary = response.text
    except (KeyError, IndexError) as e:
        flash('Error retrieving weather information. Please try again.', 'error')
        return redirect('/index')  # Redirect if there is an issue with the data structure

    return render_template('weather.html', date=date, avg_temp=avg_temp, max_temp=max_temp, min_temp=min_temp, description=description, city=city, wind_speed=wind_speed, dew=dew, pressure=pressure, humidity=humidity, summary=summary)
