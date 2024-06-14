from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from sqlalchemy.exc import SQLAlchemyError
# TODO: from app.logger import logger

from app.dao.base import BaseDAO
from app.database.connection import async_session_maker

# from sqlalchemy.exc import SQLAlchemyError
# from app.logger import logger

from app.modules.questions.dao import QuestionDAO

from .models import TopicModel
from .schemas import STopicTreeRead

class TopicDAO(BaseDAO):
    model = TopicModel

    @classmethod
    async def get_topic_tree(cls, id: int) -> STopicTreeRead:
        questions = QuestionDAO.get_all_objects(topic_id=id)
        if not questions:
            questions = []
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(selectinload(cls.model.children))
                .filter_by(id=id)
            )
            topic = await session.execute(query).scalars().one_or_none()

        children = topic.children
        if children:
            for child in children:
                await cls.get_topic_tree(child.id)
        else: 
            children = []
        return STopicTreeRead(
            id=topic.id,
            name=topic.name,
            children=children,
            questions=questions
        )
        
        
    @classmethod
    async def get_all_topics_tree(cls) -> List[STopicTreeRead]:
        result = []
        topics = cls.get_all_objects()
        for topic in topics:
            topic = await cls.get_topic_tree(topic.id)
            result.append(topic)
        return result

            
        