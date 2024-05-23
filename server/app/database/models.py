from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, MetaData, TIMESTAMP
from typing import Optional
from sqlalchemy.orm import relationship

metadata = MetaData()

class Model(DeclarativeBase):
    __abstract__ = True
    metadata = metadata

class TopicModel(Model):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("topics.id"), nullable=True)

    children: Mapped[list["TopicModel"]] = relationship("TopicModel", backref="parent", remote_side=[id])
    questions: Mapped[list["QuestionModel"]] = relationship("QuestionModel", back_populates="topic")

    def __repr__(self) -> str:
        return f"<TopicModel(id={self.id}, name={self.name}, parent_id={self.parent_id})>"

class QuestionModel(Model):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"), nullable=False)

    topic: Mapped["TopicModel"] = relationship("TopicModel", back_populates="questions")

    def __repr__(self) -> str:
        return f"<QuestionModel(id={self.id}, question={self.question}, answer={self.answer}, topic_id={self.topic_id})>"

# class SobesModel(Model):
#     __tablename__ = "sobeses"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(nullable=False)
#     # create_at: 
#     # time
#     # sum_score: Mapped(float) = mapped_colum(nullable=True)
#     # user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

# class SobesQuestionModel(Model):
#     __tablename__ = "sobes_question"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     sobes_id: Mapped[int] = mapped_column(ForeignKey("sobeses.id"), nullable=False)
#     question_id: Mapped[Optional[int]] = mapped_column(ForeignKey("questions.id"), nullable=True)
#     question: Mapped[str] = mapped_column(nullable=False)
#     answer: Mapped[str] = mapped_column(nullable=False)
#     score: Mapped[Optional[int]] = mapped_column(nullable=True)

