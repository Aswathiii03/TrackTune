# TrackTune - Plan and Overview Document

## Project Overview

TrackTune is an API service that recommends songs based on a user's mood and the current weather in their city. The application checks if the user's mood matches the current weather conditions and provides a song recommendation that aligns with their mood.

## Architecture

The application follows a simple microservices-inspired architecture with the following components:

1. **FastAPI Application**: The main application that handles HTTP requests and responses
2. **Weather Service**: Responsible for fetching weather data from OpenWeatherMap API
3. **Music Service**: Responsible for fetching song recommendations from Last.fm API
4. **Mood Matcher Service**: Responsible for determining if a mood matches the current weather conditions
5. **Recommendation Service**: Combines the above services to provide comprehensive recommendations
6. **Frontend UI**: A responsive web interface for interacting with the API

## API Endpoints

### GET /
- Serves the frontend UI for the application

### POST /recommend
- Takes a JSON payload with `mood` and `city` fields (or coordinates)
- Returns weather information, mood-weather match status, and a song recommendation

### GET /weather/{city}
- Returns weather information and suggested mood for a given city

## External APIs Used

### OpenWeatherMap API
- Used to fetch current weather data for a given city
- Provides temperature, weather conditions, and other meteorological data

### Last.fm API
- Used to fetch song recommendations based on mood tags
- Provides song title, artist, and URL information

## Mood-Weather Matching Logic

The application uses a mapping of weather conditions and temperature ranges to determine which moods are appropriate for the current weather:

1. **Weather Conditions**: Different weather conditions (Clear, Clouds, Rain, etc.) are mapped to appropriate moods
2. **Temperature**: Temperature ranges are also mapped to appropriate moods
3. **Matching**: A user's mood is considered to match the weather if it appears in either the weather condition moods or temperature moods

## Frontend UI

The application includes a responsive web interface with the following features:

1. **Mood Selection**: Dropdown menu for selecting the user's current mood
2. **City Input**: Text field for entering the user's city
3. **Results Display**: Shows weather information, mood match status, and song recommendation
4. **Error Handling**: Provides user-friendly error messages

## Implementation Details

### Technology Stack
- **FastAPI**: Modern, fast web framework for building APIs
- **Python 3.8+**: Core programming language
- **HTML/CSS/JavaScript**: Frontend UI
- **Requests**: HTTP library for making API calls
- **Pydantic**: Data validation and settings management
- **python-dotenv**: Environment variable management

### Project Structure
```
TrackTune/
├── main.py                      # FastAPI application entry point
├── requirements.txt             # Project dependencies
├── .env.example                 # Example environment variables
├── services/                    # Service modules
│   ├── __init__.py
│   ├── weather_service.py       # Weather API integration
│   ├── music_service.py         # Music API integration
│   ├── mood_matcher.py          # Mood-weather matching logic
│   └── recommendation_service.py # Combined recommendation logic
├── static/                      # Frontend files
│   ├── index.html               # Main HTML page
│   ├── styles.css               # CSS styles
│   └── script.js                # Frontend JavaScript
├── postman/                     # Postman collection for testing
│   ├── TrackTune.postman_collection.json
│   └── TrackTune.postman_environment.json
└── docs/                        # Documentation
    └── overview.md              # This document
```

## Setup and Deployment

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with API keys
4. Run the application: `uvicorn main:app --reload`

### Production Deployment
For production deployment, consider:
- Using a proper WSGI server like Gunicorn
- Setting up proper environment variable management
- Implementing rate limiting for external API calls
- Adding caching for weather data to reduce API calls

## Future Enhancements

Potential future enhancements include:
- User accounts to track preferences
- Historical mood and weather tracking
- More sophisticated mood-weather matching algorithms
- Integration with music streaming services
- Mobile application frontend