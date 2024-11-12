from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MASUPERCLESECRETE'
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
    OPENWEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5"
