import json
from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
from models.db import  SessionLocal
from pydantic import BaseModel
import models.models as models
import base64



router = APIRouter(tags=['test'])
class  Question(BaseModel):
    question_text: str

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.post("/upload")
async def upload_file(request: Request,db: Session = Depends(get_db)):
    body = json.loads(await request.body())
    """ byte_str = str.encode(body['base64_data'])
    File = models.File(data=byte_str)
    db.add(File)
    db.commit()"""
    return body
