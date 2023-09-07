from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
origins = [
    "http://127.0.0.1:5500",  # Add your frontend origin here
    # You can add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dummy-api")
def get_dummy_api():
    return {
        "song_title": "Space Cadet",
        "artist_name": "Metro Boomin'",
        "is_playing": False,
        "volume": 50,
        "progress": 0
    }

@app.get("/stream-audio")
def stream_audio():
    # Path to the audio file
    audio_file_path = os.path.join("media", "mb_space_cadet.mp3")

    # Check if the file exists
    if not os.path.exists(audio_file_path):
        return "Audio file not found", 404

    # Set the Content-Type header to indicate audio/mp3
    headers = {
        "Content-Type": "audio/mp3"
    }

    # Stream the file using FastAPI's FileResponse
    return FileResponse(audio_file_path, headers=headers)
