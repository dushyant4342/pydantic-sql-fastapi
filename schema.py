from pydantic import BaseModel
from datetime import datetime

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

class QAHistoricItem(BaseModel):
    id: int
    question: str
    answer: str
    timestamp: datetime

    class Config:
        orm_mode = True



# How Pydantic validates the Q & A

#class QuestionRequest(BaseModel):     -> question: str
  
# class AnswerResponse(BaseModel):     -> answer: str

#1. Request validation
#In main.py:
# @app.post("/ask", response_model=AnswerResponse)
# async def ask_question(req: QuestionRequest, db: Session = Depends(get_db)):
#{ "question": "What is FastAPI?" }
# Pydantic:
# Ensures the key "question" is present ✅
# Ensures it's a string ✅
# Automatically returns a 422 error if anything’s wrong ❌

#2. Response validation
#In main.py:
# @app.post("/ask", response_model=AnswerResponse)
# async def ask_question(req: QuestionRequest, db: Session = Depends(get_db)):
#{ "answer": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints." }
# Pydantic:
# Ensures the key "answer" is present ✅
# Ensures it's a string ✅
# Automatically returns a 422 error if anything’s wrong ❌





