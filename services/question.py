from sqlalchemy.orm import Session
import models.models as models
from utils.image import image_to_text
from utils.voice import voice_to_text

#SET GLOBAL max_allowed_packet = 67108864;
def create(db: Session,QuestionSchema):
    text = image_to_text(QuestionSchema['image'])
    
    print(text)
    QuestionSchema['audio'] = str.encode(QuestionSchema['audio'])
    QuestionSchema['image'] = str.encode(QuestionSchema['image'])
    voice_to_text(QuestionSchema['audio'])
    Question = models.Question(**QuestionSchema)
    db.add(Question)
    db.commit()
    return Question
 
def delete(db: Session, id: int):
    Question =db.query(models.Question).filter(models.Question.id == id).first()
    db.delete(Question)
    db.commit()

