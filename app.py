import requests

def getGeoLocationFromPlaceName(placeName) -> dict:
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={placeName}&language=en&format=json"
    response = requests.api.get(url)
    return response.json()

def getWeatherDataFromHeadings(lat, long) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code,rain,visibility,snowfall"
    response = requests.api.get(url)
    return response.json()

def main():
    print("##### py geo cli #####")
    placeName = input("Enter place name, post code or \"quit\" $ ")
    if placeName.lower() in ["quit", "q", "exit"]:
        quit()
    geoData = getGeoLocationFromPlaceName(placeName)
    print(geoData)
    if geoData.get("results"):
        print(getWeatherDataFromHeadings(geoData["results"][0]["latitude"], geoData["results"][0]["longitude"]))
    else:
        print("Location not found, check you spelt it right")
        main()

main()