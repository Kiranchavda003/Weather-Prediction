import requests
import os

API_KEY = "bcf978d91ef944c1b1c90726241403"
API_URL = "https://api.weatherapi.com/v1/forecast.json"
IMAGES_FOLDER = "images"

def get_weather_forecast(city, forecast_days=None):
    try:
        params = {
            "key": API_KEY,
            "q": city,
            "days": forecast_days or 1
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "forecast" in data:
            return data["forecast"]["forecastday"]
        else:
            print("Error: 'forecast' key not found in the API response.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_weather_icon(condition):
    if not os.path.exists(IMAGES_FOLDER):
        print(f"Error: {IMAGES_FOLDER} folder not found.")
        return None

    condition_lower = condition.lower()
    if "clear" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "clear.png")
    elif "cloud" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "cloud.png")
    elif "sunny" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "Sunny.png")
    elif "rain" in condition_lower or "shower" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "rain.png")
    elif "snow" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "snow.png")
    elif "storm" in condition_lower or "thunder" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "storm.png")
    elif "mist" in condition_lower or "fog" in condition_lower:
        return os.path.join(IMAGES_FOLDER, "mist.png")
    else:
        return None