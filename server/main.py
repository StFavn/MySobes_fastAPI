from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import questions_router, topics_router

app = FastAPI(
    title="Questions API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(questions_router)  #/questions
app.include_router(topics_router)     #/topics

# http://localhost:5173/