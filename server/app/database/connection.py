from sqlalchemy import select
from fastapi import HTTPException

from app.database.db_init import new_session
from app.database.models import QuestionModel, TopicModel
from app.schemas import SQuestion, SQuestionNoID
from app.schemas import STopic, STopicNoID, STopicTree


class TopicConnection:
    # --- CREATE ---
    @classmethod
    async def add_one(cls, data: STopicNoID) -> STopic:
        async with new_session() as session:
            topic_data = data.model_dump()
            topic = TopicModel(**topic_data)
            session.add(topic)
            await session.flush()
            await session.commit()
            topic_formated = STopic.model_validate(topic)
            return topic_formated
        
    # --- UPDATE ---
    @classmethod
    async def update(cls, topic_id: int, data: STopicNoID) -> STopic:
        async with new_session() as session:
            topic = await cls.get_by_id_model(session, topic_id)
            if not topic:
                raise HTTPException(status_code=404, detail="Topic not found")
            topic_data = data.model_dump()
            for key, value in topic_data.items():
                setattr(topic, key, value)
            await session.commit()
            await session.refresh(topic)
            topic_formated = STopic.model_validate(topic)
            return topic_formated
    
    # --- DELETE ---
    @classmethod
    async def delete_by_id(cls, topic_id: int) -> bool:
        async with new_session() as session:
            query = select(TopicModel).where(TopicModel.id == topic_id)
            result_query = await session.execute(query)
            topic = result_query.scalar()
            
            children_query = select(TopicModel).where(TopicModel.parent_id == topic_id)
            result_children_query = await session.execute(children_query)
            children = result_children_query.scalars().all()
            if children:
                for child in children:
                    child_is_deleted = await cls.delete_by_id(child.id)
                    if not child_is_deleted:
                        return False
            try:
                question_query = select(QuestionModel).where(QuestionModel.topic_id == topic_id)
                result_question_query = await session.execute(question_query)
                questions = result_question_query.scalars().all()
                if questions:
                    for question in questions:
                        await session.delete(question)

                await session.delete(topic)
            except:
                session.rollback()
                return False
            
            await session.commit()
            return True

    # --- GET ---
    @classmethod
    async def get_all(cls) -> list[STopicTree]:
        async with new_session() as session:
            query = select(TopicModel).where(TopicModel.parent_id == None)
            result_query = await session.execute(query)
            topics = result_query.scalars().all()
            if not topics: return []
            topics_result = []
            for topic in topics:
                children = await cls.get_children(topic.id)

                questions = await QuestionConnection.get_by_topic(topic.id)
                if not questions: questions = []

                topic_formated = STopicTree(
                    id=topic.id,
                    name=topic.name,
                    children=children,
                    questions=questions
                )
                topics_result.append(topic_formated)
            return topics_result

    @classmethod
    async def get_by_id_model(cls, session, topic_id: int) -> TopicModel:
        query = select(TopicModel).where(TopicModel.id == topic_id)
        result_query = await session.execute(query)
        topic = result_query.scalar()
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        return topic

    @classmethod
    async def get_by_id(cls, topic_id: int) -> STopicTree:
        async with new_session() as session:
            topic = await cls.get_by_id_model(session, topic_id)
            questions = await QuestionConnection.get_by_topic(topic_id)
            if not questions: questions = []

            children = await cls.get_children(topic_id)
            return STopicTree(
                id=topic.id,
                name=topic.name,
                children=children,
                questions=questions
            )

    @classmethod
    async def get_children(cls, parent_id: int) -> list[STopicTree]:
        async with new_session() as session:
            query = select(TopicModel).where(TopicModel.parent_id == parent_id)
            result_query = await session.execute(query)
            topics = result_query.scalars().all()
            if not topics: return []

            topics_result = []
            for topic in topics:
                children = await cls.get_children(topic.id)
                questions = await QuestionConnection.get_by_topic(topic.id)
                if not questions: questions = []
                topic_formated = STopicTree(
                    id=topic.id,
                    name=topic.name,
                    children=children,
                    questions=questions
                )
                topics_result.append(topic_formated)
            return topics_result
        
        
class QuestionConnection:
    # --- CREATE ---
    @classmethod
    async def add_one(cls, data: SQuestionNoID) -> SQuestion:
        async with new_session() as session:
            question_data = data.model_dump()
            question = QuestionModel(**question_data)
            if not await TopicConnection.get_by_id(question.topic_id):
                raise HTTPException(status_code=404, detail="Topic not found")
            session.add(question)
            await session.flush()
            await session.commit()
            question_formated = SQuestion.model_validate(question)
            return question_formated
        
    # --- UPDATE ---
    @classmethod
    async def update(cls, question_id: int, data: SQuestionNoID) -> SQuestion:
        async with new_session() as session:
            question = await cls.get_by_id_model(session, question_id)
            if not question:
                raise HTTPException(status_code=404, detail="Question not found")
            question_data = data.model_dump()
            for key, value in question_data.items():
                setattr(question, key, value)
            await session.commit()
            await session.refresh(question)
            question_formated = SQuestion.model_validate(question)
            return question_formated
        
    # --- DELETE ---
    @classmethod
    async def delete_by_id(cls, question_id: int) -> bool:
        async with new_session() as session:
            query = select(QuestionModel).where(QuestionModel.id == question_id)
            result_query = await session.execute(query)
            question = result_query.scalar()
            if not question:
                raise HTTPException(status_code=404, detail="Question not found")
            await session.delete(question)
            await session.commit()
            return True

    # --- GET ---
    @classmethod
    async def get_all(cls) -> list[SQuestion]:
        async with new_session() as session:
            query = select(QuestionModel)
            result_query = await session.execute(query)
            questions = result_query.scalars().all()
            questions_schema = [SQuestion.model_validate(question) for question in questions]
            return questions_schema
    
    @classmethod
    async def get_by_id_model(cls, session, question_id: int) -> QuestionModel:
        query = select(QuestionModel).where(QuestionModel.id == question_id)
        result_query = await session.execute(query)
        question = result_query.scalar()
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        return question

    @classmethod
    async def get_by_id(cls, question_id: int) -> SQuestion:
        async with new_session() as session:
            question = await cls.get_by_id_model(session, question_id)
            question_formated = SQuestion.model_validate(question)
            return question_formated
        
    @classmethod 
    async def get_by_topic(cls, topic_id: int) -> list[SQuestion]:
        async with new_session() as session:
            query = select(QuestionModel).where(QuestionModel.topic_id == topic_id)
            result_query = await session.execute(query)
            questions = result_query.scalars().all()
            if not questions: return []
            questions_schema = [SQuestion.model_validate(question) for question in questions]
            return questions_schema
        

        
    


