import requests
import json
import datetime as dt

def getGeoLocationFromPlaceName(placeName: str) -> list:
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={placeName}&language=en&format=json"
    response = requests.api.get(url).json()
    try:
        lat = response["results"][0]["latitude"]
        long = response["results"][0]["longitude"]
    except:
        return ["None"]
    return [lat, long]

def getWeatherDataFromHeadings(lat, long) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code"
    response = requests.api.get(url)
    return response.json()

def main():
    print("##### py geo cli #####")
    placeName = input("Enter place name, post code or \"quit\" $ ")
    if placeName.lower() in ["quit", "q", "exit"]:
        quit()
    geoData = getGeoLocationFromPlaceName(placeName)
    print(geoData)
    if geoData[0] != "None":
        forecast = getWeatherDataFromHeadings(geoData[0], geoData[1])

        weather = "null"
        if forecast.get("current"):
            with open("weatherCodes.json") as rawCodes:
                codes = json.load(rawCodes)
                weather = codes[str(forecast["current"]["weather_code"])]
        
        date = dt.datetime.fromisoformat(forecast["current"]["time"])

        print(f"\n#### {placeName} weather forecast #####\n")
        print(f"Lat: {forecast["latitude"]} Long: {forecast["longitude"]}")
        print(f"Weather: {weather}")
        print(f"date: {date.strftime("%d/%m/%y")} time: {date.strftime("%H:%M:%S")}")
        


    else:
        print("Location not found, check you spelt it right")
        main()

if __name__ == "__main__":
    main()