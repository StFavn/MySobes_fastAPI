from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.database.base_model import Base


class SobesQuestionModel(Base):
    __tablename__ = "sobes_questions"

    id:          Mapped[int] = mapped_column(primary_key=True)
    sobes_id:    Mapped[int] = mapped_column(ForeignKey("sobeses.id"))
    question:    Mapped[str]
    answer:      Mapped[str]

    user_answer: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    score:       Mapped[Optional[int]]
    duration:    Mapped[Optional[int]]

    question_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("questions.id", ondelete="SET NULL")
    )

    sobes: Mapped["SobesModel"] = relationship( # type: ignore
        back_populates="questions"
    )

    def __str__(self):
        return f'Вопрос:id - {self.id}, Текст вопроса - {self.question}'
