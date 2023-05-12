from pydantic import BaseModel

class Question(BaseModel):
    text: str
    image: str
    audio:str
    chat_id:int
    response_text:str
    response_audio:str





