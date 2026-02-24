import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
WEATHER_API_URL = os.getenv("WEATHER_API_URL")

def get_weather_data(location):
    """
    Get weather data using OpenWeatherMap API
    
    Args:
        location: City name as a string
    """
    if not OPENWEATHERMAP_API_KEY:
        raise ValueError("OpenWeatherMap API key is missing. Please set it in the .env file.")
    
    params = {
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric",  # Use metric units for temperature
        "q": location
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract relevant weather information
        weather_info = {
            "temperature": data["main"]["temp"],
            "conditions": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return weather_info
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching weather data: {str(e)}")