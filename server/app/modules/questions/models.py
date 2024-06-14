from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from app.database.base_model import Base

class QuestionModel(Base):
    __tablename__ = "questions"

    id:       Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(length=1000))
    answer:   Mapped[str] = mapped_column(String(length=5000))
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))

    parent_topic: Mapped["TopicModel"] = relationship( # type: ignore
        back_populates="questions"
    ) 

    def __str__(self):
        return f'Вопрос:id - {self.id}, Текст вопроса - {self.question}'