# Pydantic-SQL-FastAPI

A fast, production-style LLM Q&A API built using **FastAPI**, **Google Gemini**, **Pydantic**, and **SQLite with SQLAlchemy**. It showcases how to structure modern async APIs with validation, logging, and persistent storage. SQLAlchemy is an open-source Python library that provides an SQL toolkit (called "SQLAlchemy Core") and an Object Relational Mapper (ORM) for database interactions.

---

## 🔧 Tech Stack

- **FastAPI** – API framework (async + blazing fast)
- **Pydantic** – Input/output validation
- **Google Gemini API** – LLM response generation
- **SQLite + SQLAlchemy** – Lightweight database + ORM
- **Logging** – Tracks all Q&A activity

---

## ✅ How it works

1. Send a question to `POST /ask`
2. FastAPI validates it and queries Google Gemini (async)
3. The answer is returned and stored in the database
4. Use `GET /history` to retrieve past Q&As

---

## 📦 Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Add your Gemini API key in .env:
GEMINI_API_KEY=your_key_here

