from pydantic import BaseModel

class Question(BaseModel):
    text: str
    image: bytes
    audio:bytes
    chat_id:int






