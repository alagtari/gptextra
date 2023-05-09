from sqlalchemy.orm import Session
import models.models as models

def get_by_id(db: Session, id: int):
    user = db.query(models.Chat).filter(models.Chat.id == id).first()
    return user.questions

def get_all(db: Session):
    Chats = db.query(models.Chat).all()    
    try :
        Chats[0].questions
    except :
        return []
    return Chats    


def delete(db: Session, id: int):
    Chat =db.query(models.Chat).filter(models.Chat.id == id).first()
    db.delete(Chat)
    db.commit()

def create(db: Session,name:str):
    Chat = models.Chat(title=name)
    db.add(Chat)
    db.commit()
    return Chat

def update(db: Session,name:str,id:int):
    chat = db.query(models.Chat).filter(models.Chat.id == id).first()
    chat.title = name
    db.commit()
    db.refresh(chat)
    return chat