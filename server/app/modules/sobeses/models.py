from datetime import datetime
from sqlalchemy.sql import func

from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime

from app.database.base_model import Base

class SobesModel(Base):
    __tablename__ = "sobeses"

    id:              Mapped[int] = mapped_column(primary_key=True)
    duration:        Mapped[Optional[int]]
    status:          Mapped[str] = mapped_column(default="created")
    average_score:   Mapped[Optional[float]]
    count_questions: Mapped[Optional[int]]


    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    questions: Mapped[list["SobesQuestionModel"]] = relationship(  # type: ignore
        back_populates="sobes", cascade='all, delete-orphan'
    )

    def __str__(self):
        return f'Собес:id - {self.id}, Создан - {self.create_at}'



    
    