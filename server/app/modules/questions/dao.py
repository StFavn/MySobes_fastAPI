from typing import List
from app.dao.base import BaseDAO

from .models import QuestionModel

class QuestionDAO(BaseDAO):
    model = QuestionModel

    @classmethod
    async def get_questions_by_parent_id_list(cls, parent_id_list) -> List[QuestionModel]:
        questions_result = []
        for parent_id in parent_id_list:
            questions = await cls.get_all_objects(parent_id=parent_id)
            questions_result.extend(questions)
        return questions_result