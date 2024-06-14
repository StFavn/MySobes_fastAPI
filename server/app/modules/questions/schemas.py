from pydantic import BaseModel

class SQuestionRead(BaseModel):
    """Схема чтения вопросоа."""

    id:       int
    question: str
    answer:   str
    topic_id: int


class SQuestionCreate(BaseModel):
    """Схема создания вопроса."""

    question: str
    answer:   str
    topic_id: int

class SQuestionUpdate(BaseModel):
    """Схема обновления вопроса."""

    question: str | None = None
    answer:   str | None = None
    topic_id: int | None = None