from fastapi import FastAPI, Request
import requests
import os
from dotenv import load_dotenv
import uvicorn

# .env faylini yuklash
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

        # API strukturasiga qarab barcha media URL larini olish
        # Bu yerda "media" key bo'lishi kerak, agar boshqacha bo'lsa API docs ga qarab o'zgartiring
        media_list = data.get("media", [])
        urls = [item.get("url") for item in media_list if item.get("url")]

        return {"success": True, "media_urls": urls}

    except Exception as e:
        return {"success": False, "error": str(e)}

# Render-da 24/7 ishlash uchun uvicorn
if __name__ == "__main__":
    uvicorn.run("Instagram:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), log_level="info")
