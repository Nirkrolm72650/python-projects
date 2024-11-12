from flask import Blueprint, render_template, request, flash
from WeatherApp.app.services.weather_services import WeatherService
import requests

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        try:
            weather_service = WeatherService()
            weather_data = weather_service.get_weather_by_city(city)
        except requests.exceptions.HTTPError as e:
            flash(f"Erreur lors de la récupération des données météo: {str(e)}")

    return render_template('index.html', weather=weather_data)
