# 🚀 Gemini AI YouTube Automation System

An end-to-end **AI-powered YouTube automation framework** that analyzes video content and automatically generates optimized metadata, schedules uploads, and publishes videos using the YouTube Data API.

Powered by **Google Gemini (Vertex AI)**, **Speech-to-Text**, and **YouTube Data API v3**.

---

## ✨ Features

- 🎬 **Automatic Video Content Analysis**
  - Extracts audio from videos
  - Transcribes speech using Google Speech-to-Text
  - Understands video context intelligently

- 🧠 **AI-Generated Metadata (Gemini)**
  - SEO-optimized **Title**
  - High-retention **Description**
  - Viral **Tags & Hashtags**
  - Language auto-selection (English / Hindi / Hinglish)

- ⏰ **Auto Scheduling**
  - Uploads videos with future scheduling
  - One-video-per-day strategy to avoid spam & limits

- 🚫 **Duplicate Protection**
  - Prevents re-uploading the same video
  - Maintains upload history

- 📁 **Auto File Management**
  - Uploaded videos are moved automatically

---

## 📂 Project Structure

youtube_automation/
│
├── main.py # Main automation runner
├── gemini_metadata.py # Gemini AI + Speech analysis logic
├── auth.py # YouTube OAuth authentication
│
├── videos/ # Raw videos to upload
├── uploaded/ # Uploaded videos (auto-moved)
│
├── database.json # Upload history
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md

## Google Cloud Setup

Enable the following APIs in Google Cloud Console:
YouTube Data API v3
Vertex AI API
Speech-to-Text API
Billing (required)

## Credentials Required

OAuth Client ID
Download as client_secret.json
Service Account Key
- Download and rename to:

your_service_account.json

## 🔐 Authentication

Run once to authenticate YouTube:

python auth.py

This generates token.pkl for future uploads.

## ▶️ Run the Automation

cd youtube_automation
python main.py


## The system will:

Analyze video content
Generate AI-based title, description & tags
Schedule upload
Upload video to YouTube
Update database
Move uploaded video to uploaded/

## 🧠 AI Intelligence

Gemini automatically:
Understands video context from audio
Chooses best language (English / Hindi / Hinglish)
Generates SEO-optimized, viral metadata
Adapts tone for kids, storytelling, or general content


## ⚠️ Notes

YouTube daily upload limits apply
Google Cloud billing is mandatory
Recommended: run once per day

## 🎯 Use Cases

Kids & Cartoon Channels
Faceless YouTube Automation
Educational Content
Storytelling & Motivation
Scalable Content Pipelines

## 📜 Disclaimer

This project is for educational and automation purposes only.
Users are responsible for compliance with YouTube and Google Cloud policies.

