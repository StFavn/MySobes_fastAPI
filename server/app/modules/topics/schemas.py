from pydantic import BaseModel
from app.modules.questions.schemas import SQuestionRead

class STopicRead(BaseModel):
    """Схема чтения вопросоа."""

    id:        int
    name:      str
    parent_id: int | None = None


class STopicTreeRead(BaseModel):
    """Схема чтения вопросоа."""

    id:        int
    name:      str
    children:  list["STopicTreeRead"]
    questions: list["SQuestionRead"]

class STopicCreate(BaseModel):
    """Схема создания вопроса."""

    name:      str
    parent_id: int | None = None

class STopicUpdate(BaseModel):
    """Схема обновления вопроса."""

    name:      str | None = None
    parent_id: int | None = None