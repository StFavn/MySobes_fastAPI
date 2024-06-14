# from typing import Optional
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey, String

# from app.database.base_model import Base

# class SobesQuestionModel(Base):
#     __tablename__ = "sobes_questions"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     sobes_id: Mapped[int] = mapped_column(ForeignKey("sobeses.id"), nullable=False)
#     question_id: Mapped[Optional[int]] = mapped_column(ForeignKey("questions.id"), nullable=True)
#     question: Mapped[str] = mapped_column(nullable=False)
#     answer: Mapped[str] = mapped_column(nullable=False)
#     user_answer: Mapped[str] = mapped_column(nullable=True)
#     score: Mapped[Optional[int]] = mapped_column(nullable=True)

#     sobes = relationship("SobesModel", back_populates="questions")

#     def __repr__(self) -> str:
#         return (f"<SobesQuestionModel(id={self.id}, sobes_id={self.sobes_id}, question_id={self.question_id}, "
#                 f"question={self.question}, answer={self.answer}, "
#                 f"user_answer={self.user_answer}, score={self.score})>")
    


    
    