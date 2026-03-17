import json
import datetime as dt
import logging

from apis import getGeoLocationFromPlaceName, getWeatherDataFromHeadings

logging.basicConfig(
    filename="log.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime}, {levelname}, {name}, {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

def exportForecast(forecast: str) -> None:
    try:
        with open("history.csv", "r+") as f:
            if f.read() == "":
                f.write("Time, Place name, Lat, Long, Weather code, Weather")
    except:
        with open("history.csv", "w") as f:
            f.write("Time, Place name, Lat, Long, Weather code, Weather")

    with open("history.csv", "a") as f:
        logging.info("writing forecast to history.csv")
        f.write("\n" + forecast)

def main():
    print("##### py geo cli #####")
    try:
        placeName = input("Enter place name or type \"quit\" $ ")
    except:
        quit()
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

        if input("save to file \"Y/n\" ? $ ").lower() == "y":
            data = f"{forecast["current"]["time"]}, {placeName}, {forecast["latitude"]}, {forecast["longitude"]}, {forecast["current"]["weather_code"]}, {weather}"
            exportForecast(data)
        
        logging.info("successful forecast, ending program")

    else:
        logging.warning("no place name entered, retrying")
        print("Location not found, check you spelt it right")
        main()

if __name__ == "__main__":
    main()