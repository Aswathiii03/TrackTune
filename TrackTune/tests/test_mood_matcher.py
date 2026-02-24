"""
Unit tests for the mood_matcher module.
"""
import unittest
from services.mood_matcher import (
    match_mood_with_weather,
    get_temperature_mood,
    get_suggested_mood,
    WEATHER_TO_MOOD
)

class TestMoodMatcher(unittest.TestCase):
    """Test cases for the mood_matcher module functions."""
    
    def test_get_temperature_mood(self):
        """Test that temperature ranges return the correct moods."""
        self.assertEqual(get_temperature_mood(-5), ["melancholic", "calm"])
        self.assertIn("relaxed", get_temperature_mood(5))
        self.assertIn("nostalgic", get_temperature_mood(15))
        self.assertIn("happy", get_temperature_mood(25))
        self.assertIn("excited", get_temperature_mood(35))
        
    def test_get_temperature_mood_invalid_input(self):
        """Test that get_temperature_mood raises TypeError for invalid inputs."""
        with self.assertRaises(TypeError):
            get_temperature_mood("not a number")
    
    def test_match_mood_with_weather_matching(self):
        """Test that matching moods return True."""
        # Test with Clear weather and warm temperature
        weather_data = {"conditions": "Clear", "temperature": 25}
        self.assertTrue(match_mood_with_weather("happy", weather_data))
        self.assertTrue(match_mood_with_weather("energetic", weather_data))
        
        # Test with Rain weather and cool temperature
        weather_data = {"conditions": "Rain", "temperature": 5}
        self.assertTrue(match_mood_with_weather("melancholic", weather_data))
        
    def test_match_mood_with_weather_non_matching(self):
        """Test that non-matching moods return False."""
        weather_data = {"conditions": "Clear", "temperature": 25}
        self.assertFalse(match_mood_with_weather("sad", weather_data))
        
    def test_match_mood_with_weather_case_insensitive(self):
        """Test that mood matching is case insensitive."""
        weather_data = {"conditions": "Clear", "temperature": 25}
        self.assertTrue(match_mood_with_weather("HAPPY", weather_data))
        self.assertTrue(match_mood_with_weather("Happy", weather_data))
        
    def test_match_mood_with_weather_invalid_input(self):
        """Test that match_mood_with_weather handles invalid inputs."""
        with self.assertRaises(ValueError):
            match_mood_with_weather("", {"conditions": "Clear", "temperature": 25})
            
        with self.assertRaises(TypeError):
            match_mood_with_weather("happy", "not a dict")
            
        with self.assertRaises(KeyError):
            match_mood_with_weather("happy", {"conditions": "Clear"})
            
        with self.assertRaises(KeyError):
            match_mood_with_weather("happy", {"temperature": 25})
            
    def test_get_suggested_mood(self):
        """Test that get_suggested_mood returns a valid mood."""
        weather_data = {"conditions": "Clear", "temperature": 25}
        mood = get_suggested_mood(weather_data)
        self.assertIn(mood, ["happy", "energetic", "romantic", "excited"])
        
        weather_data = {"conditions": "Rain", "temperature": 5}
        mood = get_suggested_mood(weather_data)
        self.assertIn(mood, ["sad", "melancholic", "nostalgic", "calm", "relaxed"])
        
    def test_get_suggested_mood_invalid_input(self):
        """Test that get_suggested_mood handles invalid inputs."""
        with self.assertRaises(KeyError):
            get_suggested_mood({"conditions": "Clear"})
            
        with self.assertRaises(KeyError):
            get_suggested_mood({"temperature": 25})

if __name__ == '__main__':
    unittest.main()