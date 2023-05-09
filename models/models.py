from sqlalchemy import Column, Integer, String, ForeignKey,LargeBinary
from sqlalchemy.orm import relationship
from .db import Base

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    questions = relationship('Question', backref='chat')

class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    question_text = Column(String(255))
    response_text = Column(String(255))
    chat_id = Column(Integer, ForeignKey('chat.id'))
    image = Column(LargeBinary(length=(2**32)-1))
    audio = Column(LargeBinary(length=(2**32)-1))
    response_audio = Column(LargeBinary(length=(2**32)-1)) 





