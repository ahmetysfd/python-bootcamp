import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "3bac4e88f67a52186b7cbc5c22155ad3"

weather_params = {
    "lat": 51.759445,
    "lon": 19.457216,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

# Check for rain in the forecast
for forecast in weather_data["list"]:
    weather_id = forecast["weather"][0]["id"]
    if weather_id < 700:
        print("Bring an umbrella.")
