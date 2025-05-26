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
