from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Tuple
import uvicorn
import os
from pathlib import Path
from services.recommendation_service import get_weather_based_recommendation

app = FastAPI(
    title="TrackTune API",
    description="API that recommends songs based on mood and weather",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

class MoodRequest(BaseModel):
    mood: Optional[str] = None
    city: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Serve the index.html file
    html_path = Path("static/index.html")
    if html_path.exists():
        with open(html_path, "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    else:
        return HTMLResponse(content=f"<html><body><h1>Error: File not found</h1><p>Path: {html_path.absolute()}</p></body></html>")

@app.post("/recommend")
async def recommend_song(request: MoodRequest):
    try:
        # Get recommendation based on weather and optional mood
        recommendation = get_weather_based_recommendation(
            request.city, 
            user_mood=request.mood
        )
        
        return {
            "location": request.city,
            "city": request.city,
            "weather": recommendation["weather"],
            "mood": recommendation["mood"],
            "mood_matches_weather": recommendation["mood_matches_weather"],
            "song_recommendation": recommendation["song_recommendation"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/weather/{city}")
async def get_weather(city: str):
    try:
        recommendation = get_weather_based_recommendation(city)
        return {
            "location": city,
            "weather": recommendation["weather"],
            "suggested_mood": recommendation["mood"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)