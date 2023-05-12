from fastapi import Depends,APIRouter, File, UploadFile,Request,Form
from sqlalchemy.orm import Session
import services.question as question
from models.db import  SessionLocal
from pydantic import BaseModel
from schemas import Question as QuestionSchema
import json


router = APIRouter(tags=['projects'])
class  Question(BaseModel):
    question_text: str

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()



@router.post("/question")
async def create( request : Request ,db: Session = Depends(get_db)):

        body = json.loads(await request.body())

        response = question.create(db,body)
        return response


@router.get("/questions/{id}")
def get_all( id : int ,db: Session = Depends(get_db)):
        questions = question.get_by_chat_id(db,id)
        return {"status" : 200 , "data" : questions }

@router.delete("/question/{id}")
def get_all( id: int,db: Session = Depends(get_db)):

        questions = question.delete(db,id)
        return {"status" : 200 , "message" : 'question deleted' }

