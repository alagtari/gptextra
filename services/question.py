from sqlalchemy.orm import Session
import models.models as models
from schemas import Question as QuestionSchema

def create(db: Session,QuestionSchema):
    QuestionSchema['audio'] = str.encode(QuestionSchema['audio'])
    QuestionSchema['image'] = str.encode(QuestionSchema['image'])
    Question = models.Question(**QuestionSchema)
    db.add(Question)
    db.commit()
    return Question

def delete(db: Session, id: int):
    Question =db.query(models.Question).filter(models.Question.id == id).first()
    db.delete(Question)
    db.commit()

