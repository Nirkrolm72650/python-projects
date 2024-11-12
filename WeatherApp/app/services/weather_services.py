import requests
from WeatherApp.app.models.weather import Weather
from flask import current_app

class WeatherService:
    def __init__(self):
        self.api_key = current_app.config['OPENWEATHER_API_KEY']
        self.base_url = current_app.config['OPENWEATHER_BASE_URL']

    def get_weather_by_city(self, city: str) -> Weather:
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        return Weather.from_api_response(response.json())
