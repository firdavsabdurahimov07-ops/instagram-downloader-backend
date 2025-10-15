from fastapi import FastAPI, Request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

@app.get("/")
def home():
    return {"message": "✅ Instagram Downloader Backend ishlayapti!"}

@app.get("/download")
def download_instagram(url: str):
    try:
        api_url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/index"
        headers = {
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
        }
        params = {"url": url}

        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()

        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
