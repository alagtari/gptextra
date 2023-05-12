from sqlalchemy.orm import Session
import models.models as models
from utils.image import image_to_text
from utils.voice import voice_to_text
from utils.chatgpt import chat_completion
from utils.outputaudio import audio
import os
import base64
from utils.formatresponse import format
import openai
import re
from utils.scrap import scrap
#SET GLOBAL max_allowed_packet = 68719476736;
def get_by_chat_id(db: Session,id):
    questions = db.query(models.Question).filter(models.Question.chat_id == id)

    response_questions = []
    for Question in questions :
        formatted  = format(Question.response_text)
        if bytes(Question.audio) == b'':
            audio = None
        else:
            audio = Question.audio
        question = {
        "id": Question.id,
        "question_text": Question.question_text,
        "image": Question.image,
        "audio": audio,
        "response_text":formatted,
        "response_audio":Question.response_audio
        }
        response_questions.append(question)
    return response_questions

def create(db: Session,QuestionSchema):
    text = ''
    if os.path.exists('output.wav') :
        with open('output.wav', 'rb') as audio_file:
              audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes)
        QuestionSchema['audio'] = audio_base64
        try :
            audio_text = voice_to_text()
            text += audio_text+"."
        except :
             QuestionSchema['error'] = "Speech cannot be recognized !"
             return {"status" : 404  , "data" : QuestionSchema}
        

    if 'question_text' in QuestionSchema.keys() :
        text += QuestionSchema['question_text']+"."
        
    print('image' in QuestionSchema.keys())

    if 'image' in QuestionSchema.keys():
        tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        if not os.path.exists(tesseract_path):
            QuestionSchema['error'] = "you must install tesseract.exe to enable image recognition "
            return {"status" : 404  , "data" : QuestionSchema}
        
        image_text = image_to_text(QuestionSchema['image'])
        QuestionSchema['image'] = str.encode(QuestionSchema['image'])
        text += image_text+"."

    if os.path.exists('output.wav') :
        os.remove('output.wav')

    text = scrap(text)
    print(text)

    try :
        chatgpt_response= chat_completion(text)
    except openai.error.APIError as e:
        QuestionSchema['error'] =  "An error occurred while processing your request. Please try again later or contact support if the problem persists."
        return {"status" : 404 , "data" : QuestionSchema } 
        
    except openai.error.APIConnectionError as e:
        QuestionSchema['error'] = "Unable to connect to the API server. Please check your internet connection and try again later."
        return {"status" : 404 , "data" : QuestionSchema } 
        
    except openai.error.RateLimitError as e:
        QuestionSchema['error'] = "You have exceeded the rate limit for this API. Please wait a few minutes and try again later."
        return {"status" : 404 , "data" : QuestionSchema } 
    
    except openai.error.AuthenticationError as e:
        QuestionSchema['error'] = "You should check your API key and make sure it is valid and authorized to access the API."
        return {"status" : 404 , "data" : QuestionSchema } 
        


    QuestionSchema["response_text"] = chatgpt_response
    
    audio(chatgpt_response[:600])
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

