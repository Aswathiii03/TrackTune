from services.weather_service import get_weather_data
from services.music_service import get_song_recommendation
from services.mood_matcher import match_mood_with_weather

def get_weather_based_recommendation(location, user_mood=None):
    """
    Get song recommendations based on current weather and optional user mood
    
    Args:
        location: City name as a string
        user_mood: Optional user-specified mood. If None, mood will be derived from weather
    
    Returns:
        Dictionary containing weather data, mood, and song recommendation
    """
    # Get current weather data
    weather_data = get_weather_data(location)
    
    # If user didn't specify a mood, determine it from weather
    if not user_mood:
        # Get moods associated with current weather condition
        weather_condition = weather_data["conditions"]
        from services.mood_matcher import WEATHER_TO_MOOD, get_temperature_mood
        
        weather_moods = WEATHER_TO_MOOD.get(weather_condition, [])
        temp_moods = get_temperature_mood(weather_data["temperature"])
        
        # Use the first mood from combined list
        all_moods = list(set(weather_moods + temp_moods))
        if all_moods:
            mood = all_moods[0]
        else:
            mood = "relaxed"  # Default mood if no match
    else:
        mood = user_mood
        
    # Check if user's mood matches the weather (only if user provided a mood)
    mood_matches_weather = None
    if user_mood:
        mood_matches_weather = match_mood_with_weather(user_mood, weather_data)
    
    # Get song recommendation based on mood
    song_recommendation = get_song_recommendation(mood)
    
    return {
        "weather": {
            "description": weather_data["description"],
            "temperature": weather_data["temperature"],
            "conditions": weather_data["conditions"]
        },
        "mood": mood,
        "mood_matches_weather": mood_matches_weather,
        "song_recommendation": song_recommendation
    }