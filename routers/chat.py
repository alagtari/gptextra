from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
import services.chat as chat
from models.db import  SessionLocal

router = APIRouter(tags=['projects'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@router.get("/chat/{id}")
def get_by_id(id:int,db: Session = Depends(get_db)):
        questions = chat.get_by_id(db,id)
        return {"status" : 200 , "data" : questions }

@router.get("/chat")
def get_all(db: Session = Depends(get_db)):
        chats = chat.get_all(db)
        return {"status" : 200 , "data" : chats }

@router.post("/chat/{name}")
def get_all( name:str,db: Session = Depends(get_db)):

        chats = chat.create(db,name)
        return {"status" : 200 , "data" : chats }

@router.put("/chat")
def get_all( name : str ,id : int,db: Session = Depends(get_db)):

        updated_chat = chat.update(db,name,id)
        return {"status" : 200 , "data" : updated_chat }

@router.delete("/chat/{id}")
def get_all( id: int,db: Session = Depends(get_db)):

        chat.delete(db,id)
        return {"status" : 200 , "message" : 'chat deleted' }

    

