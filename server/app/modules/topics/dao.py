from typing import List
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# TODO: from sqlalchemy.exc import SQLAlchemyError
# TODO: from app.logger import logger

from app.dao.base import BaseDAO
from app.database.connection import async_session_maker

from app.modules.questions.dao import QuestionDAO

from .models import TopicModel
from .schemas import STopicTreeRead

class TopicDAO(BaseDAO):
    model = TopicModel

    @classmethod
    async def get_topic_tree(cls, id: int):
        topic = await cls.get_object(id=id)
        if not topic:
            return None

        questions = await QuestionDAO.get_all_objects(topic_id=id)
        if not questions:
            questions = []

        children = []
        children_tree = await cls.get_all_objects(parent_id=id)
        if children_tree:
            for child in children_tree:
                child = await cls.get_topic_tree(child.id)
                children.append(child)
        

        return STopicTreeRead(
            id=topic.id,
            name=topic.name,
            children=children,
            questions=questions
        )
            
        
    @classmethod
    async def get_all_topics_tree(cls) -> List[STopicTreeRead]:
        result = []
        topics = await cls.get_all_objects(parent_id=None)
        for topic in topics:
            topic = await cls.get_topic_tree(topic.id)
            result.append(topic)
        return result

            
        