import httpx
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#GEMINI_URL = f"https://generative-language.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
#GEMINI_URL = f"https://generative-language.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"


GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
async def ask_gemini(prompt: str) -> str:
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(GEMINI_URL, headers=headers, json=body)
            response.raise_for_status()
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"


print("🔑 Gemini API Key:", GEMINI_API_KEY)
