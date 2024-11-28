import requests
import json
from datetime import datetime
import google.generativeai as genai

api_key = 'RVD4YVGCKQTA7DFNYM4FMSPD7'
city = 'Oklahoma'
base_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&include=current%2Cevents%2Calerts&key={api_key}&contentType=json'
weather_data = requests.get(base_url)
weather_json = (weather_data.json())['days'][0]
location = weather_data.json()['resolvedAddress']


genai.configure(api_key="AIzaSyC29PlZiwWLucDkpuFBTxllQwUjJ7TCNTE")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"I am building a flask weather app, you are a professional news reporter analyze the weather data in {weather_json} and produce short concise report for my weather app , include suggestion and cautions. A one line short summary of the weather and a one line short suggestion on activities or what to wear and/or a caution")
print(response.text)