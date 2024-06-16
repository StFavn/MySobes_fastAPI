from pydantic import BaseModel

class SSobesQuestionRead(BaseModel):
    """Схема чтения вопросоа."""

    id:          int
    sobes_id:    int
    question_id: int | None = None
    question:    str
    answer:      str
    user_answer: str | None = None
    score:       int | None = None


class SSobesQuestionUpdate(BaseModel):
    """Схема обновления вопроса."""

    user_answer: str | None = None
    score:       int | None = None
