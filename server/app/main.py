from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.questions.router import router as questions_router
from app.modules.topics.router import router as topics_router

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

app.include_router(topics_router)     #/topics
app.include_router(questions_router)  #/questions

# http://localhost:5173/