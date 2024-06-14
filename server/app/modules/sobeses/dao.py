# # from app.dao.base import BaseDAO

# # from .models import TopicModel

# # class TopicDAO(BaseDAO):
# #     model = TopicModel

# from sqlalchemy import select
# from fastapi import HTTPException
# from datetime import datetime, timezone
# import random 

# from app.modules.models import SobesModel, SobesQuestionModel
# from app.modules.schemas import SSobes, SSobesQuestion, SSobesFilters
# from app.connection.question_conn import QuestionConnection

# from app.database.db_init import get_current_session
# new_session = get_current_session()

# class SobesConnection:
#     # --- CREATE ---
#     @classmethod
#     async def create_sobes(cls, sobes_filters: SSobesFilters) -> SSobes:
#         async with new_session() as session:
#             # Создание нового контейнера sobes
#             sobes = SobesModel(
#                 name="New Sobes",
#                 create_at=datetime.now(timezone.utc),
#                 status=False
#             )
#             session.add(sobes)
#             await session.flush()  # Сохраняем чтобы получить ID
#             await session.commit()
#             # Создание списка вопросов для нового контейнера sobes
#             sobes_questions = await cls.create_question_list(sobes.id, sobes_filters)

#             # Создание Pydantic объекта SSobes
#             sobes_formated = SSobes(
#                 id=sobes.id,
#                 name=sobes.name,
#                 create_at=sobes.create_at,
#                 end_at=sobes.end_at,
#                 duration_seconds=sobes.duration_seconds,
#                 status=sobes.status,
#                 questions=sobes_questions,
#                 questions_count=len(sobes_questions)
#             )
#             return sobes_formated

#     @classmethod
#     async def create_question_list(cls, sobes_id: int, sobes_filters: SSobesFilters) -> list[SSobesQuestion]:
#         async with new_session() as session:
#             all_questions_orm = await QuestionConnection.get_all_model(session)
#             random.shuffle(all_questions_orm)

#             # Проверка на достаточное количество вопросов
#             if len(all_questions_orm) < sobes_filters.questions_count:
#                 selected_questions = all_questions_orm
#             else:
#                 selected_questions = all_questions_orm[:sobes_filters.questions_count]
            
#             sobes_questions = []
#             for question in selected_questions:
#                 sobes_question = SobesQuestionModel(
#                     sobes_id=sobes_id,
#                     question_id=question.id,
#                     question=question.question,
#                     answer=question.answer,
#                     user_answer=None,
#                     score=None
#                 )
#                 session.add(sobes_question)
#                 await session.flush()  # Для получения сгенерированного id
#                 sobes_questions.append(SSobesQuestion.model_validate(sobes_question))

#             await session.commit()
#             return sobes_questions

#     # -- GET --
#     @classmethod
#     async def get_sobes_by_id(cls, sobes_id: int) -> SSobes:
#         async with new_session() as session:
#             # Извлечение контейнера sobes по его идентификатору
#             sobes_query = select(SobesModel).where(SobesModel.id == sobes_id)
#             result_sobes_query = await session.execute(sobes_query)
#             sobes = result_sobes_query.scalar()
#             if sobes is None:
#                 raise HTTPException(status_code=404, detail="Sobes not found")
            
#             question_query = select(SobesQuestionModel).where(SobesQuestionModel.sobes_id == sobes_id)
#             result_question_query = await session.execute(question_query)
#             questions = result_question_query.scalars().all()
#             questions_schema = [SSobesQuestion.model_validate(question) for question in questions]

#             sobes_schema = SSobes(
#                 id=sobes.id,
#                 name=sobes.name,
#                 create_at=sobes.create_at,
#                 end_at=sobes.end_at,
#                 duration_seconds=sobes.duration_seconds,
#                 status=sobes.status,
#                 questions=questions_schema,
#                 questions_count=len(questions)
#             )
#             return sobes_schema