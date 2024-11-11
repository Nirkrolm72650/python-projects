import requests
import json

api_key="e5fc209fac428ce640b587c06b972fc3"

BASE_URL="https://api.openweathermap.org/data/2.5/weather?"


city_name= input("Entrez une ville : ")

url = BASE_URL  + "&q=" + city_name + "&lang=fr" + "&appid=" + api_key + "&units=metric"


response = requests.get(url)
data = response.json()

print(f"Nous sommes à {city_name}")
print(f"Il fait actuellement {int(data['main']['temp'])} C°")
print(f"Description du temps : {data['weather'][0]['description']}")