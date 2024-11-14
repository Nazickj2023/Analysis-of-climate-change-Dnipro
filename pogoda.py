import requests
import json

API_KEY = "7388094d817cdcd20833300dbc6b50e3"
CITY_NAME = "Dnipro,UA"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&lang=ua&units=metric"
response = requests.get(URL)
if response.status_code == 200:
    data_dict = json.loads(response.content)
    city = data_dict["name"]
    country = data_dict["sys"]["country"]
    temperature = data_dict["main"]["temp"]
    weather_description = data_dict["weather"][0]["description"]
    humidity=data_dict["main"]["humidity"]

 