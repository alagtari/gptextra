from fastapi import FastAPI
import  models.models as models
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from models.db import  engine
import uvicorn
import routers.chat as chat
import routers.question as question
import routers.test as test
from utils.record import record


models.Base.metadata.create_all(bind=engine)   
    

app = FastAPI()

# Allow requests from any origin 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/record')
async def root():
    record()

app.include_router(chat.router)
app.include_router(question.router)
app.include_router(test.router)


if __name__ == "__main__":
    uvicorn.run("main:app",  port=8000 ,reload=True)            

    