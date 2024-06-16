from datetime import datetime
from pydantic import BaseModel
from app.modules.sobes_questions.schemas import SSobesQuestionRead

class SSobesRead(BaseModel):
    """Схема чтения собеса."""

    id:              int
    create_at:       datetime
    status:          str
    count_questions: int
    average_score:   float | None = None
    duration:        int | None = None
    questions:       list[SSobesQuestionRead]



class SSobesCreate(BaseModel):
    """Схема создания собеса."""

    topic_id_list:   list[int]
    count_questions: int

class SSobesUpdate(BaseModel):
    """Схема обновления собеса."""

    status:   str | None = None
    duration: int | None = None
