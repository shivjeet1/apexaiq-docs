import requests as re
from flask import request, jsonify
from secrets import secrets
from __main__ import app

class weather_api:
    KEY = secrets['WEATHER']

    def get_latlong(self, city) -> dict:
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={self.KEY}"
        location = re.get(url)
        latlong = {'lat': location.json()[0]["lat"],
                   'long': location.json()[0]["long"]}
        return latlong

    def get_weather(self, city):
        latlong = self.get_latlong(city)
        lat = latlong['lat']
        long = latlong['long']
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&long={long}&appid={self.KEY}"
        weather = re.get(url).json()
        cache = {key: weather_info[key] for key in ['name', 'main', 'weather']}
        """cache.update{{'timestamp': time.time()}}"""
        return jsonify(cache)

forecast = weather_api()

@app.get("/weather")
def weather_api():
    city = request.args.get('city')
    if not city:
        return "City not specified"
    return forecast.get_weather(city)




