import unittest
from unittest.mock import patch
from datetime import datetime
from WeatherApp.app.models.weather import Weather
from WeatherApp.app.services.weather_services import WeatherService


class TestWeatherService(unittest.TestCase):
    @patch('app.services.weather_service.requests.get')
    def test_get_weather_by_city(self, mock_get):
        # Données de test
        mock_response = {
            "name": "Paris",
            "sys": {
                "country": "FR"
            },
            "weather": [
                {
                    "description": "sunny",
                    "icon": "01d"
                }
            ],
            "main": {
                "temp": 293.15,
                "humidity": 60
            },
            "dt": 1636721400
        }
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200

        # Appel du service
        weather_service = WeatherService()
        weather = weather_service.get_weather_by_city("Paris")

        # Vérifications
        self.assertIsInstance(weather, Weather)
        self.assertEqual(weather.city, "Paris")
        self.assertEqual(weather.country, "FR")
        self.assertEqual(weather.description, "sunny")
        self.assertEqual(weather.icon, "01d")
        self.assertEqual(weather.temperature, 20.0)
        self.assertEqual(weather.humidity, 60)
        self.assertEqual(weather.timestamp, datetime.fromtimestamp(1636721400))

    @patch('app.services.weather_service.requests.get')
    def test_get_weather_by_city_error(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = Exception("API error")

        weather_service = WeatherService()
        with self.assertRaises(Exception):
            weather_service.get_weather_by_city("Invalid City")


if __name__ == '__main__':
    unittest.main()
