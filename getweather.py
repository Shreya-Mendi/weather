import requests
import os
import pandas as pd
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    # print(data)
    # print(data.keys())   
    
    # 5. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    humid = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    #6 Return results
    result = {
        "city": city_name,
        "temp": temp,
        "humidity": humid,
        "description": description,
    }

    return result, None

def weatherforecast(city):
    """Fetch 5-day forecast (3-hour intervals)."""
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    resp = requests.get(url, params=params).json()

    # dataframe of forecast
    forecast_data = []
    for item in resp["list"]:
        forecast_data.append({
            "datetime": pd.to_datetime(item["dt"], unit="s"),
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "desc": item["weather"][0]["description"]
        })
    df = pd.DataFrame(forecast_data)
    return df, None

    # 6. Print
    # print(f"In {city_name}, it is {temp}°C with {description} and a humidity of {humid}%.")

# Try it
#if __name__ == "__main__":
# city = input("Enter the name of your city: ")
# get_weather(city)
