# TrackTune

TrackTune is an application that recommends songs based on the user's mood and current weather in their city. It checks if the mood matches the weather and suggests appropriate songs.



## Features

- Takes user's mood and city as input
- Fetches current weather data for the specified city
- Determines if the mood matches the current weather
- Recommends a song that matches the user's mood
- Provides detailed weather information and song details
- Elegant and responsive user interface

## Demo

Visit the application at [http://localhost:8000](http://localhost:8000) after setting it up.

## Setup

1. download the Zip file
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your API keys:
   ```
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   LASTFM_API_KEY=your_lastfm_api_key
   ```
4. Run the application:
   ```
   uvicorn main:app --reload
   ```
5. Open your browser and navigate to [http://localhost:8000](http://localhost:8000)

## API Endpoints

### GET /
- Serves the frontend UI

### POST /recommend
- Request body:
  ```json
  {
    "mood": "happy",
    "city": "New York"
  }
  ```
- Response:
  ```json
  {
    "location": "New York",
    "city": "New York",
    "weather": {
      "description": "clear sky",
      "temperature": 22.5,
      "conditions": "Clear"
    },
    "mood": "happy",
    "mood_matches_weather": true,
    "song_recommendation": {
      "title": "Happy",
      "artist": "Pharrell Williams",
      "url": "https://www.last.fm/music/Pharrell+Williams/_/Happy",
      "mood": "happy"
    }
  }
  ```

### GET /weather/{city}
- Returns weather information and suggested mood for a given city

## API Services Used

- **Weather Data**: OpenWeatherMap API
- **Song Recommendations**: Last.fm API

## Postman Collection

A Postman collection is included in the `postman` directory for testing the API endpoints.

## Project Structure

```
TrackTune/
├── main.py                      # FastAPI application entry point
├── services/                    # Service modules
│   ├── weather_service.py       # Weather API integration
│   ├── music_service.py         # Music API integration
│   ├── mood_matcher.py          # Mood-weather matching logic
│   └── recommendation_service.py # Combined recommendation logic
├── static/                      # Frontend files
│   ├── index.html               # Main HTML page
│   ├── styles.css               # CSS styles
│   └── script.js                # Frontend JavaScript
├── postman/                     # Postman collection for testing
└── docs/                        # Documentation
```

## Technologies Used

- **Backend**: FastAPI, Python
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: OpenWeatherMap, Last.fm
- **Documentation**: Postman Collection


