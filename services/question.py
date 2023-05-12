from sqlalchemy.orm import Session
import models.models as models
import schemas
from utils.image import image_to_text
from utils.voice import voice_to_text
from utils.main import chat_completion
from utils.outputaudio import audio
import os
import base64
from utils.formatresponse import format


#SET GLOBAL max_allowed_packet = 68719476736;
def get_by_chat_id(db: Session,id):
    questions = db.query(models.Question).filter(models.Question.chat_id == id)

    response_questions = []
    for Question in questions :
        formatted  = format(Question.response_text)
        question = {
        "id": Question.id,
        "question_text": Question.question_text,
        "image": Question.image,
        "audio": Question.audio,
        "response_text":formatted,
        "response_audio":Question.response_audio
        }
        response_questions.append(question)
    return response_questions

def create(db: Session,QuestionSchema):
    text = ''
    if 'question_text' in QuestionSchema.keys() :
        text += QuestionSchema['question_text']+"."
    if 'image' in QuestionSchema.keys():
        print("image")
        image_text = image_to_text(QuestionSchema['image'])
        QuestionSchema['image'] = str.encode(QuestionSchema['image'])
        text += image_text+"."

    if os.path.exists('output.wav') :
        try :
            audio_text = voice_to_text()
        except :
             return {"status" : 404 , "data" : "Speech cannot be recognized !" }
        text += audio_text+"."
        with open('output.wav', 'rb') as audio_file:
              audio_bytes = audio_file.read()
              
        # Encode audio bytes as base64
        audio_base64 = base64.b64encode(audio_bytes)
        QuestionSchema['audio'] = audio_base64
        
    if os.path.exists('output.wav') :
        os.remove('output.wav')
    try :
        chatgpt_response= chat_completion(text)
    except :
         return {"status" : 404 , "data" : "Request too long !" }    

    QuestionSchema["response_text"] = chatgpt_response
    
    audio(chatgpt_response[:800])
    with open('response.wav', 'rb') as audio_file:
              audio_bytes = audio_file.read()
        # Encode audio bytes as base64
    audio_base64 = base64.b64encode(audio_bytes)
    QuestionSchema['response_audio'] = audio_base64

    Question = models.Question(**QuestionSchema)
    db.add(Question)
    db.commit()
    formatted  = format(QuestionSchema["response_text"])
    question = {
        "id": Question.id,
        "question_text": Question.question_text,
        "image": Question.image,
        "audio": Question.audio,
        "response_text":formatted,
        "response_audio":Question.response_audio
    }
    return {"status" : 200 , "data" : question }
    

 
def delete(db: Session, id: int):
    Question =db.query(models.Question).filter(models.Question.id == id).first()
    db.delete(Question)
    db.commit()

