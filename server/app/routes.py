from fastapi import APIRouter

from app.database.connection import QuestionConnection
from app.schemas import SQuestionNoID, SQuestion

from app.database.connection import TopicConnection
from app.schemas import STopicAdd, STopic, STopicTree

from app.schemas import SResponse

# --- QUESTIONS ---
questions_router = APIRouter(
    prefix="/questions",
    tags=["questions"]
)

@questions_router.get("")
async def get_all_questions() -> list[SQuestion]:
    questions = await QuestionConnection.get_all()
    return questions

@questions_router.post("")
async def add_question(question: SQuestionNoID) -> SQuestion:
    question = await QuestionConnection.add_one(question)
    return question

@questions_router.get("/{question_id}")
async def get_question_by_id(question_id: int) -> SQuestion:
    question = await QuestionConnection.get_by_id(question_id)
    return question

@questions_router.put("/{question_id}")
async def edit_question(question_id: int, question: SQuestionNoID) -> SQuestion:
    updated_question = await QuestionConnection.update(question_id, question)
    return updated_question

@questions_router.delete("/{question_id}")
async def delete_question_by_id(question_id: int) -> SResponse:
    result = await QuestionConnection.delete_by_id(question_id)
    if result: return SResponse(message="OK", code=200)
    else: return SResponse(message="Bad request", code=400)

# --- TOPICS ---
topics_router = APIRouter(
    prefix="/topics",
    tags=["topics"]
)

@topics_router.post("")
async def add_topic(topic: STopicAdd) -> STopic:
    topic = await TopicConnection.add_one(topic)
    return topic

@topics_router.get("")
async def get_all_topics() -> list[STopicTree]:
    topics = await TopicConnection.get_all()
    return topics

@topics_router.get("/{topic_id}")
async def get_topic_by_id(topic_id: int) -> STopicTree:
    topic = await TopicConnection.get_by_id(topic_id)
    return topic

@topics_router.put("/{topic_id}")
async def edit_topic(topic_id: int, topic: STopicAdd) -> STopic:
    updated_topic = await TopicConnection.update(topic_id, topic)
    return updated_topic

@topics_router.delete("/{topic_id}")
async def delete_topic_by_id(topic_id: int) -> SResponse:
    result = await TopicConnection.delete_by_id(topic_id)
    if result: return SResponse(message="OK", code=200)
    else: return SResponse(message="Bad request", code=400)






