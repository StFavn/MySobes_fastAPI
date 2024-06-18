# from typing import List
import random
from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError

from app.dao.base import BaseDAO
from app.database.connection import async_session_maker
from app.logger import logger

from app.modules.sobes_questions.dao import SobesQuestionDAO
from app.modules.questions.dao import QuestionDAO

from .models import SobesModel
from .schemas import SSobesRead, SSobesUpdate

class SobesDAO(BaseDAO):
    model = SobesModel

    @classmethod
    async def create_sobes(
        cls, topic_id_list, count_questions
    ) -> SSobesRead:
        """Добавление нового собеса."""
        questions = []
        for topic_id in topic_id_list:
            questions_by_topic = await QuestionDAO.get_all_objects(topic_id=topic_id)
            if not questions_by_topic:
                questions_by_topic = []
            questions.extend(questions_by_topic)

        if not questions:
            return None
        
        random.shuffle(questions)
        if len(questions) > count_questions:
            questions = questions[:count_questions]

        sobes = await cls.add_object(status="created", count_questions=len(questions))
        if not sobes:
            return None
        
        sobes_id = sobes.id

        # TODO: добавить try-except
        for question in questions:
            sobes_question = await SobesQuestionDAO.add_object(
                sobes_id=sobes_id, 
                question_id=question.id,
                question=question.question,
                answer=question.answer
            )

        sobes = await cls.get_sobes_by_id(id=sobes_id)
        if not sobes:
            return None
        return sobes
    

    @classmethod
    async def get_sobes_by_id(cls, id: int) -> SSobesRead:
        """Возвращение одного sobes-контейнера по id."""
        try:
            async with async_session_maker() as session:
                query = (
                    select(SobesModel)
                    .filter_by(id=id)
                    .options(selectinload(SobesModel.questions))
                )
                result = await session.execute(query)
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        return jsonable_encoder(result.scalars().one_or_none())


    @classmethod
    async def get_all_sobeses(cls, **kwargs) -> List[SSobesRead]:
        """Возвращение всех sobes-контейнеров."""

        try:
            async with async_session_maker() as session:
                query = (
                    select(SobesModel)
                    .filter_by(**kwargs)
                    .options(selectinload(SobesModel.questions))
                    .order_by(SobesModel.create_at.desc())
                )
                result_execute = await session.execute(query)
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        sobeses = result_execute.scalars().all()
        return jsonable_encoder(sobeses)
    

    @classmethod
    async def recalculate_score(cls, sobes_id: int) -> SSobesRead:
        """Перерасчет average_score для собеса."""

        sobes_questions = await SobesQuestionDAO.get_all_objects(sobes_id=sobes_id)

        scored_questions_count = 0
        score_sum = 0
        duration_sum = 0
        for question in sobes_questions:
            if question.score is not None:
                scored_questions_count += 1
                score_sum += question.score
                duration_sum += question.duration

        if scored_questions_count > 0:
            async with async_session_maker() as session:
                query = select(SobesModel).filter_by(id=sobes_id)
                sobes = await session.execute(query)
                sobes = sobes.scalars().one_or_none()
                sobes.average_score = round(score_sum / scored_questions_count, 2)
                sobes.duration = duration_sum
    
                session.add(sobes)
                await session.commit()
        
        sobes = await cls.get_sobes_by_id(id=sobes_id)
        return sobes
        