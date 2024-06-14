from app.dao.base import BaseDAO

from .models import QuestionModel

class QuestionDAO(BaseDAO):
    model = QuestionModel