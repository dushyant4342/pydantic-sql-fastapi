Run in the terminal
sqlite3 gemini-2-flash.db
SELECT * FROM qa_history order by timestamp desc LIMIT 2;




🧠 "Ask Llama2" – LLM Q&A API

Build a FastAPI-based microservice that:
🔍 Accepts a user question via an API
📦 Validates input with Pydantic
⚙️ Calls Gemini Model API (async)
📝 Logs each request/response
💾 Stores history in a PostgreSQL DB using SQLAlchemy + Alembic
🧪 Adds unit + integration tests to ensure reliability


You’ll learn:
FastAPI routing
Async programming with HTTP calls
Pydantic models
Logging/debugging
DB migrations
Writing tests


├── main.py                # FastAPI app
├── models.py              # SQLAlchemy models
├── database.py            # DB connection setup
├── schema.py              # Pydantic request/response models
├── ollama_client.py       # Llama2 API wrapper
├── logger.py              # Basic logging setup
├── test_main.py           # Basic test
├── alembic/               # (init later with Alembic)
└── requirements.txt


 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


 🧠 How the app works
1. User sends a question to /ask via POST

{
  "question": "What is FastAPI?"
}

2. main.py handles the request

@app.post("/ask")
async def ask_question(req: QuestionRequest, db: Session = Depends(get_db))
Validates input with Pydantic

Logs it using logger

Calls ask_llama2(prompt) (defined in ollama_client.py) to get LLaMA2's response

3. LLaMA2 response fetched using HTTP (async)
response = await client.post("http://localhost:11434/api/generate", json={...})
Ollama must be running locally (ollama run llama2)

4. Response saved to DB
record = QAHistory(question=req.question, answer=answer)
db.add(record)
db.commit()

5. Answer is returned as JSON
{
  "answer": "FastAPI is a web framework for building APIs..."
}
💽 How the DB part works
SQLite is used with SQLAlchemy

Table qa_history stores: ID, question, answer, and timestamp

Models defined in models.py

DB setup in database.py

🧪 How to test
Use test_main.py:
