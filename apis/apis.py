import json
import requests
import logging

logging.basicConfig(
    filename="log.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime}, {levelname}, {name}, {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

def getGeoLocationFromPlaceName(placeName: str) -> list:
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={placeName}&language=en&format=json"
    response = requests.api.get(url).json()
    try:
        lat = response["results"][0]["latitude"]
        long = response["results"][0]["longitude"]
    except:
        logging.error("Invalid lat & long returented due to invalid place name")
        return ["None"]
    return [lat, long]

def getWeatherDataFromHeadings(lat, long) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code"
    response = requests.api.get(url)
    if response:
        return response.json()
    else:
        logging.error("invalid response from met API")
        return {}