from fastapi.testclient import TestClient  
from main import app

client = TestClient(app)

def test_ask_question():
    res = client.post("/ask", json={"question": "What is FastAPI?"})
    assert res.status_code == 200
    assert "answer" in res.json()


#pytest test_main.py

# ✅ Why write tests?
# 💥 Catch bugs early
# 🔁 Verify your code still works after changes
# ✅ Ensure inputs/outputs behave as expected

#🔄 Starts your app in memory
#🚀 Sends a test POST request to /ask
#✅ Checks:
#Status is 200 OK
#Response has "answer" key

