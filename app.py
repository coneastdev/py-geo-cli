import requests

def getGeoLocationFromPlaceName(placeName):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={placeName}&language=en&format=json"
    response = requests.api.get(url)
    return response.json()

def getWeatherDataFromHeadings(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41"

def main():
    print("##### py geo cli #####")
    placeName = input("Enter place name, post code or \"quit\" $ ")
    if placeName.lower() in ["quit", "q", "exit"]:
        quit()
    print(getGeoLocationFromPlaceName(placeName))

main()