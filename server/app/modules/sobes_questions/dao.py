# from typing import List
from app.dao.base import BaseDAO

from .models import SobesQuestionModel

class SobesQuestionDAO(BaseDAO):
    model = SobesQuestionModel