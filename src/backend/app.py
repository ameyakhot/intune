from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import os
import boto3
import io

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the AWS S3 client
s3 = boto3.client('s3')

# Define your S3 bucket name and the audio file key
s3_bucket_name = 'intune-music-files'
audio_file_key = 'mb_space_cadet.mp3'

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
    try:
        # Retrieve the audio file from S3
        audio_file = s3.get_object(Bucket=s3_bucket_name, Key=audio_file_key)
        
        # Get the audio file's data
        audio_data = audio_file['Body'].read()

        # Set the Content-Type header to indicate audio/mp3
        headers = {
            "Content-Type": "audio/mp3"
        }

        # Stream the file using FastAPI's StreamingResponse
        return StreamingResponse(io.BytesIO(audio_data), headers=headers)
    
    except Exception as e:
        return "Audio file not found", 404
