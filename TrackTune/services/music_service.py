import os
import requests
from dotenv import load_dotenv

load_dotenv()

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
LASTFM_API_URL = os.getenv("LASTFM_API_URL")

# Mapping moods to Last.fm tags
MOOD_TO_TAG = {
    "happy": "happy",
    "sad": "sad",
    "energetic": "energetic",
    "relaxed": "chill",
    "angry": "angry",
    "romantic": "romantic",
    "melancholic": "melancholy",
    "excited": "upbeat",
    "calm": "calm",
    "nostalgic": "nostalgic"
}

def get_song_recommendation(mood):
    """
    Get song recommendation based on mood using Last.fm API
    """
    if not LASTFM_API_KEY:
        raise ValueError("Last.fm API key is missing. Please set it in the .env file.")
    
    # Convert mood to a tag that Last.fm understands
    tag = MOOD_TO_TAG.get(mood.lower(), mood.lower())
    
    params = {
        "method": "tag.gettoptracks",
        "tag": tag,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": 10  # Get top 10 tracks for the mood
    }
    
    try:
        response = requests.get(LASTFM_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Check if we have tracks in the response
        if "tracks" in data and "track" in data["tracks"] and data["tracks"]["track"]:
            tracks = data["tracks"]["track"]
            
            # Select a track (for simplicity, we'll take the first one)
            selected_track = tracks[0]
            
            return {
                "title": selected_track["name"],
                "artist": selected_track["artist"]["name"],
                "url": selected_track["url"],
                "mood": mood
            }
        else:
            # Fallback if no tracks found for the specific mood
            params["tag"] = "alternative"  # Use a generic tag
            response = requests.get(LASTFM_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "tracks" in data and "track" in data["tracks"] and data["tracks"]["track"]:
                selected_track = data["tracks"]["track"][0]
                return {
                    "title": selected_track["name"],
                    "artist": selected_track["artist"]["name"],
                    "url": selected_track["url"],
                    "mood": mood,
                    "note": "No exact match for your mood, showing an alternative recommendation"
                }
            else:
                return {"error": "No songs found for the given mood"}
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching song recommendations: {str(e)}")