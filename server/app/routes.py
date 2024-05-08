from fastapi import APIRouter, Body
from typing_extensions import Annotated

from app.database.connection import QuestionConnection
from app.schemas import SQuestionAdd, SQuestion

from app.database.connection import TopicConnection
from app.schemas import STopicAdd, STopic, STopicTree

from app.schemas import SResponse

# --- QUESTIONS ---
questions_router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)

@questions_router.post("")
async def add_question(question: SQuestionAdd = Body(...)) -> SQuestion:
    question = await QuestionConnection.add_one(question)
    return question

@questions_router.delete("/{question_id}")
async def delete_question_by_id(question_id: int) -> SResponse:
    result = await QuestionConnection.delete_by_id(question_id)
    if result: return SResponse(message="OK", code=200)
    else: return SResponse(message="Bad request", code=400)

@questions_router.get("")
async def get_all_questions() -> list[SQuestion]:
    questions = await QuestionConnection.get_all()
    return questions

@questions_router.get("/{question_id}")
async def get_question_by_id(question_id: int) -> SQuestion:
    question = await QuestionConnection.get_by_id(question_id)
    return question


# --- TOPICS ---
topics_router = APIRouter(
    prefix="/topics",
    tags=["topics"]
)

@topics_router.post("")
async def add_topic(topic: STopicAdd = Body(...)) -> STopic:
    topic = await TopicConnection.add_one(topic)
    return topic

@topics_router.delete("/{topic_id}")
async def delete_topic_by_id(topic_id: int) -> SResponse:
    result = await TopicConnection.delete_by_id(topic_id)
    if result: return SResponse(message="OK", code=200)
    else: return SResponse(message="Bad request", code=400)

@topics_router.get("")
async def get_all_topics() -> list[STopicTree]:
    topics = await TopicConnection.get_all()
    return topics

@topics_router.get("/{topic_id}")
async def get_topic_by_id(topic_id: int) -> STopicTree:
    topic = await TopicConnection.get_by_id(topic_id)
    return topic




