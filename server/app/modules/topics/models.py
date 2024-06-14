from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from app.database.base_model import Base

class TopicModel(Base):
    __tablename__ = "topics"

    id:        Mapped[int] = mapped_column(primary_key=True)
    name:      Mapped[str] = mapped_column(String(length=500))
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("topics.id"))

    children:  Mapped[list["TopicModel"]] = relationship(
        backref="parent", remote_side=[id], cascade='all, delete-orphan'
    )
    questions: Mapped[list["QuestionModel"]] = relationship(  # type: ignore
        back_populates="parent_topic", cascade='all, delete-orphan'
    )
    
    def __str__(self):
        return f'Тема:id - {self.id}, Название - {self.name}'
    


    
    