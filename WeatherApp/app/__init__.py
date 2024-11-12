from flask import Flask
from WeatherApp.config.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from WeatherApp.app.routes import weather_bp
    app.register_blueprint(weather_bp)

    return app
