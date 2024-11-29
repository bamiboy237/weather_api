## Weather App
A simple Flask application that displays weather information for a given city.

## Features
Displays weather information for a given city.
Uses OpenWeatherMap API to fetch weather data.
Stores weather data in Redis cache.
Uses Google Generative AI API to generate a short summary of the weather.
Uses Flask-Limiter to prevent excessive requests.
Requirements
Python 3.8 or higher
Flask 2.0.1 or higher
Requests 2.25.1 or higher
Redis 3.5.3 or higher
Flask-Limiter 1.0.0 or higher
Google-Cloud-GenerativeAI 0.1.0 or higher

## Installation
Clone the repository:
git clone https://github.com/your-username/weather-app.git

# Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt

# Set environment variables:
Create a .env file in the application root directory.

# Add the following environment variables to the file:

OPENWEATHERMAP_API_KEY=your-openweathermap-api-key
REDIS_HOST=localhost
REDIS_PORT=6379
GOOGLE_API_KEY=your-google-api-key

## Run the application:
python app.py

## Usage
Open the application in a web browser:
http://localhost:5000/

Enter a city name in the form and click "Submit".

View weather information for the city.

Testing
To run tests, use the following command:

python test.py

## Deployment
To deploy the application, you can use a variety of hosting options, including:

Heroku
PythonAnywhere
Glitch


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! See the CONTRIBUTING file for more information.

Acknowledgments
OpenWeatherMap for providing weather data.
Redis for providing a caching solution.
Flask-Limiter for providing rate limiting.
Google Generative AI for providing a text generation API.
