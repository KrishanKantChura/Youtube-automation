import os, json, shutil, pickle
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from gemini_metadata import generate_metadata

VIDEOS_DIR = "videos"
UPLOADED_DIR = "uploaded"
DB_FILE = "database.json"

os.makedirs(UPLOADED_DIR, exist_ok=True)

uploaded = json.load(open(DB_FILE)) if os.path.exists(DB_FILE) else []

creds = pickle.load(open("token.pkl", "rb"))
youtube = build("youtube", "v3", credentials=creds)
print("YouTube client ready ✅")

schedule_time = datetime.now(timezone.utc) + timedelta(days=1)

for video in os.listdir(VIDEOS_DIR):
    if video in uploaded:
        continue

    print(f"Processing: {video}")

    title, desc, hashtags, tags = generate_metadata(video)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": desc + "\n\n" + hashtags,
                "tags": tags.split(",")
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": schedule_time.isoformat()
            }
        },
        media_body=MediaFileUpload(os.path.join(VIDEOS_DIR, video))
    )

    response = request.execute()
    print("Uploaded:", response["id"])

    shutil.move(
        os.path.join(VIDEOS_DIR, video),
        os.path.join(UPLOADED_DIR, video)
    )

    uploaded.append(video)
    json.dump(uploaded, open(DB_FILE, "w"), indent=2)

    schedule_time += timedelta(hours=24)
