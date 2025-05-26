from fastapi.testclient import TestClient  # ✅ Not starlette!
from main import app

client = TestClient(app)

def test_ask_question():
    res = client.post("/ask", json={"question": "What is FastAPI?"})
    assert res.status_code == 200
    assert "answer" in res.json()
