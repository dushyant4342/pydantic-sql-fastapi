
🧠 "Ask Gemini2" – LLM Q&A API

Build a FastAPI-based microservice that:

🔍 Accepts a user question via an API

📦 Validates input with Pydantic

⚙️ Calls Gemini Model API (async)

📝 Logs each request/response

💾 Stores history in a PostgreSQL DB using SQLAlchemy + Alembic

🧪 Adds unit + integration tests to ensure reliability

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Learning points:

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
├── gemini_client.py       # gemini2 API wrapper
├── logger.py              # Basic logging setup
├── test_main.py           # Basic test
├── alembic/               # (init later with Alembic)
└── requirements.txt


 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



🧠 How the App Works (Short Summary)

1. User sends a POST request to /ask with:
   {
     "question": "What is FastAPI?"
   }

2. main.py handles it:
   - @app.post("/ask")
   - Validates with Pydantic (schema.py)
   - Logs with logger
   - Calls ask_gemini() from gemini_client.py

3. Gemini API (gemini-2.0-flash) is called asynchronously:
   await client.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent", ...)

4. Response is stored in SQLite via SQLAlchemy:
   record = QAHistory(question=req.question, answer=answer)
   db.add(record); db.commit()

5. JSON response is returned:
   {
     "answer": "FastAPI is a web framework for building APIs..."
   }

💽 How the DB Works

- Uses SQLite + SQLAlchemy
- Table: qa_history
  - id: int (primary key)
  - question: text
  - answer: text
  - timestamp: datetime
- DB path set in database.py as:
  DATABASE_URL = "sqlite:///./gemini2.db"

🧪 How to Test

1. Unit test:
   pytest test_main.py

2. Manual test via curl:
   curl -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "What is FastAPI?"}'

3. Try in Swagger UI:
   http://localhost:8000/docs

✅ Bonus:
- /history route supports optional ?q=keyword&limit=10
- Results ordered by timestamp (latest first)



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


🧠 What is async / await?
async marks a function as asynchronous — it can pause and wait.

await pauses execution until something (usually I/O) completes.

It’s like saying:
“Start this task, let me know when you're done — meanwhile, I’ll handle other things.”

Use async def to make a function non-blocking

Use await to pause and wait for external tasks (like HTTP)


@app.post("/ask")
async def ask_question(...):
This lets FastAPI handle multiple requests concurrently.


response = await client.post(...)
Sends the request to Gemini
await tells Python:
👉 “Pause here until Gemini responds — don’t block the whole server!”


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

If you're running this on your machine via:
uvicorn main:app --reload

Then your base API endpoint is:
http://localhost:8000


API routes:
POST /ask – Send a question, get an answer from Gemini

GET /history – View previously asked Q&A

You can explore all endpoints here:
http://localhost:8000/docs



🧠Explain this project:

I built an Q&A API using FastAPI and Google Gemini.

You send it a question, it gives you an answer using an LLM.

It uses Pydantic to validate inputs, stores every question/answer in a database,

and supports history search. It’s async, fast, and structured like a real microservice.

