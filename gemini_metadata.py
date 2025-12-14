import os
import subprocess
from google.genai import Client
from google.cloud import speech

client = Client(
    vertexai=True,
    project="youtube-uplode-481119",
    location="us-central1"
)

speech_client = speech.SpeechClient()

def extract_audio(video_path):
    audio_path = video_path.replace(".mp4", ".wav")
    subprocess.run([
        "ffmpeg", "-y", "-i", video_path,
        "-ac", "1", "-ar", "16000", audio_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return audio_path

def transcribe(audio_path):
    with open(audio_path, "rb") as f:
        audio = speech.RecognitionAudio(content=f.read())

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="hi-IN",
        enable_automatic_punctuation=True
    )

    response = speech_client.recognize(config=config, audio=audio)
    return " ".join(r.alternatives[0].transcript for r in response.results)

def generate_metadata(video_file):
    video_path = os.path.join("videos", video_file)
    audio = extract_audio(video_path)
    transcript = transcribe(audio)

    prompt = f"""
Analyze this cartoon video transcript and generate:
1. Best YouTube Title (Hindi / Hinglish / English – whichever suits)
2. SEO Description (story + emotions + keywords)
3. 5 Hashtags
4. 15 Viral Ranking Tags (comma separated)

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt]
    )

    text = response.text.strip().split("\n")

    title = text[0]
    description = text[1]
    hashtags = text[2]
    tags = ",".join(text[3:])

    return title, description, hashtags, tags
