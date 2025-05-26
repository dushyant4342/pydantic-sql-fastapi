import httpx

import httpx

def ask_gemini2(prompt: str) -> str:
    try:
        with httpx.Client(timeout=60) as client:
            response = client.post(
                "http://127.0.0.1:11434/api/generate",
                json={
                    "model": "llama2",
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
    except httpx.TimeoutException:
        return "❌ LLaMA2 timed out. Is Ollama running?"
    except Exception as e:
        return f"❌ Error calling LLaMA2: {str(e)}"


# async def ask_gemini2(prompt: str) -> str:
#     try:
#         async with httpx.AsyncClient(timeout=120) as client:  # ⏱ longer timeout
#             response = await client.post(
#                 "http://localhost:11434/api/generate",
#                 json={
#                     "model": "llama2",
#                     "prompt": prompt,
#                     "stream": False  # ✅ disables streaming
#                 }
#             )
#             response.raise_for_status()
#             return response.json()["response"]
#     except httpx.TimeoutException:
#         return "❌ LLaMA2 timed out. Is Ollama running?"
#     except Exception as e:
#         return f"❌ Error calling LLaMA2: {str(e)}"

#Ollama streams multiple partial chunks in a response. If stream is not set to False, response.json() fails because it expects a single JSON object.

# curl -X POST http://localhost:11434/api/generate \
#   -H "Content-Type: application/json" \
#   -d '{
#     "model": "llama2",
#     "prompt": "What is Pydantic?",
#     "stream": false
# }'


# curl -X POST http://localhost:8000/ask \
#   -H "Content-Type: application/json" \
#   -d '{"question": "What is Python?"}'
