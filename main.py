from fastapi import FastAPI, Depends
from schema import QuestionRequest, AnswerResponse
from database import SessionLocal, engine
from models import Base, QAHistory
from gemini_client import ask_gemini
from logger import logger
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from typing import List
from fastapi.responses import JSONResponse
from schema import QAHistoricItem
from fastapi import Query

load_dotenv()
app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/history", response_model=List[QAHistoricItem])
# def get_history(db: Session = Depends(get_db)):
#     history = db.query(QAHistory).order_by(QAHistory.timestamp.desc()).all()
#     return history

# @app.get("/history", response_model=List[QAHistoricItem])
# def get_history(
#     q: str = Query(None, description="Filter by keyword in question"),
#     db: Session = Depends(get_db)
# ):
#     query = db.query(QAHistory).order_by(QAHistory.timestamp.desc())

#     if q:
#         query = query.filter(QAHistory.question.ilike(f"%{q}%"))

#     return query.all()

@app.get("/history", response_model=List[QAHistoricItem])
def get_history(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(QAHistory).order_by(QAHistory.timestamp.desc()).limit(limit).all()



@app.post("/ask", response_model=AnswerResponse)
async def ask_question(req: QuestionRequest, db: Session = Depends(get_db)):
    logger.info(f"Received question: {req.question}")
    answer = await ask_gemini(req.question)
    logger.info(f"Gemini response: {answer}")

    record = QAHistory(question=req.question, answer=answer)
    db.add(record)
    db.commit()

    return {"answer": answer}


#python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GEMINI_API_KEY'))"
#uvicorn main:app --reload                                                                               


#  curl -X POST http://localhost:8000/ask \
#   -H "Content-Type: application/json" \
#  -d '{"question": "What is a Machine?"}'

# OR

#Try it on UI at http://localhost:8000/docs

# GitHub Link of the repo 🔗 https://github.com/dushyant4342/pydantic-sql-fastapi

# To try the project:
# Clone the repo
# Add a .env file with your Gemini API key (free from Google AI Studio)
# Run the app: uvicorn main:app --reload

# Access the API via FastAPI UI: http://localhost:8000/docs

# Or use it directly from the terminal:

# Ask a question:
# curl -X POST http://localhost:8000/ask \
# -H "Content-Type: application/json" \
# -d '{"question": "What is Asynchronous programming?"}'

# Get recent Q&A history:
# curl -X GET "http://localhost:8000/history?limit=3"



