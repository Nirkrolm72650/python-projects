from dataclasses import dataclass
from datetime import datetime

@dataclass
class Weather:
    temperature: float
    humidity: int
    description: str
    city: str
    country: str
    icon: str
    timestamp: datetime

    @classmethod
    def from_api_response(cls, data):
        return cls(
            temperature=data['main']['temp'] - 273.15, # Permet la conversion Kelvin vers Celsius
            humidity=data['main']['humidity'],
            description=data['weather'][0]['description'],
            city=data['name'],
            country=data['sys']['country'],
            icon=data['weather'][0]['icon'],
            timestamp=datetime.fromtimestamp(data['dt'])
        )
