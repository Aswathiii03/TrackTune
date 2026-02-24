"""
Mood Matcher Service

This module provides functionality to match user moods with weather conditions.
It maps different weather conditions and temperature ranges to corresponding moods,
and provides functions to check if a user's mood matches the current weather.

Author: TrackTune Team
"""

from typing import List, Dict, Any, Optional

# Mapping weather conditions to moods
WEATHER_TO_MOOD: Dict[str, List[str]] = {
    "Clear": ["happy", "energetic", "romantic", "excited"],
    "Clouds": ["melancholic", "nostalgic", "calm", "relaxed"],
    "Rain": ["sad", "melancholic", "nostalgic"],
    "Drizzle": ["relaxed", "calm", "melancholic"],
    "Thunderstorm": ["angry", "energetic", "excited"],
    "Snow": ["calm", "nostalgic", "romantic"],
    "Mist": ["melancholic", "calm", "relaxed"],
    "Fog": ["melancholic", "calm", "relaxed"],
    "Haze": ["melancholic", "calm", "relaxed"]
}

def get_temperature_mood(temp: float) -> List[str]:
    """
    Determine appropriate moods based on temperature ranges.
    
    Args:
        temp: Temperature in Celsius
        
    Returns:
        List of mood strings associated with the temperature range
    """
    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be a number")
        
    if temp < 0:
        return ["melancholic", "calm"]
    elif temp < 10:
        return ["calm", "relaxed", "melancholic"]
    elif temp < 20:
        return ["relaxed", "calm", "nostalgic"]
    elif temp < 30:
        return ["happy", "energetic", "romantic"]
    else:
        return ["energetic", "excited", "happy"]

def match_mood_with_weather(mood: str, weather_data: Dict[str, Any]) -> bool:
    """
    Check if the user's mood matches the current weather conditions.
    
    Args:
        mood: User's current mood as a string
        weather_data: Dictionary containing weather information with at least
                     'conditions' and 'temperature' keys
    
    Returns:
        Boolean indicating whether the mood matches the weather
        
    Raises:
        KeyError: If weather_data is missing required keys
        ValueError: If mood is empty
    """
    if not mood:
        raise ValueError("Mood cannot be empty")
    
    if not isinstance(weather_data, dict):
        raise TypeError("Weather data must be a dictionary")
        
    # Validate required keys in weather_data
    required_keys = ["conditions", "temperature"]
    for key in required_keys:
        if key not in weather_data:
            raise KeyError(f"Weather data missing required key: {key}")
    
    mood = mood.lower()
    
    # Get moods associated with current weather condition
    weather_condition = weather_data["conditions"]
    weather_moods = WEATHER_TO_MOOD.get(weather_condition, [])
    
    # Get moods associated with current temperature
    temp_moods = get_temperature_mood(weather_data["temperature"])
    
    # Combine all weather-related moods
    all_weather_moods = list(set(weather_moods + temp_moods))
    
    # Check if user's mood is in the list of weather-related moods
    return mood in all_weather_moods

def get_suggested_mood(weather_data: Dict[str, Any]) -> str:
    """
    Suggest a mood based on current weather conditions.
    
    Args:
        weather_data: Dictionary containing weather information with at least
                     'conditions' and 'temperature' keys
    
    Returns:
        A suggested mood string based on the weather
        
    Raises:
        KeyError: If weather_data is missing required keys
    """
    # Validate required keys in weather_data
    required_keys = ["conditions", "temperature"]
    for key in required_keys:
        if key not in weather_data:
            raise KeyError(f"Weather data missing required key: {key}")
    
    # Get moods associated with current weather condition
    weather_condition = weather_data["conditions"]
    weather_moods = WEATHER_TO_MOOD.get(weather_condition, [])
    
    # Get moods associated with current temperature
    temp_moods = get_temperature_mood(weather_data["temperature"])
    
    # Combine all weather-related moods and pick the first one
    all_moods = list(set(weather_moods + temp_moods))
    
    return all_moods[0] if all_moods else "relaxed"  # Default to relaxed if no moods found