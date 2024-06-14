from typing import List

from fastapi import APIRouter

# TODO: for UserModel
# from fastapi import Depends
# from app.modules.users.manager import current_superuser
# from app.modules.users.models import UserModel

# TODO: for exceptions
# from app.exceptions import (
#     DatabaseErrorException,
#     NotFoundException,
#     ObjectAlreadyExistsException
# )

from .dao import QuestionDAO
from .schemas import SQuestionCreate, SQuestionRead, SQuestionUpdate

router = APIRouter(
    prefix='/questions',
    tags=['questions']
)


@router.post('', response_model=SQuestionRead)
async def create_question(data: SQuestionCreate): # user: UserModel = Depends(current_superuser
    """Добавление нового вопроса."""

    # question_exists = await QuestionDAO.get_object(
    #     name=data.name
    #     topic_id=data.topic_id
    # )
    # if question_exists:
    #     raise ObjectAlreadyExistsException
    
    new_question = await QuestionDAO.add_object(**data.model_dump())
    # if not new_question:
    #     raise DatabaseErrorException(
    #         detail='Не удалось добавить запись в базу данных.'
    #     )
    return new_question


@router.get('/{question_id}', response_model=SQuestionRead)
async def get_question(question_id: int):
    """Возвращение вопроса по id."""

    question = await QuestionDAO.get_object(id=question_id)
    # if not question:
    #     raise NotFoundException
    return question


@router.get('', response_model=List[SQuestionRead])
async def get_questions():
    """Возвращение всех вопросов."""

    questions = await QuestionDAO.get_all_objects()
    # if not questions:
    #     raise NotFoundException
    return questions


@router.get('/topic/{topic_id}', response_model=List[SQuestionRead])
async def get_questions(topic_id: int):
    """Возвращение всех вопросов по теме."""

    questions = await QuestionDAO.get_all_objects(topic_id=topic_id)
    # if not questions:
    #     raise NotFoundException
    return questions


@router.patch('/{question_id}', response_model=SQuestionRead)
async def update_question( # user: UserModel = Depends(current_superuser
    question_id: int,
    update_data: SQuestionUpdate
):
    """Обновление данных вопроса."""

    question = await QuestionDAO.update_object(
        update_data=update_data, id=question_id
    )

    # if not question:
    #     raise DatabaseErrorException(detail='Не удалось обновить данные.')
    return question


@router.delete('/{question_id}')
async def delete_question(question_id: int): # user: UserModel = Depends(current_superuser)
    """Удаление вопроса."""

    result = await QuestionDAO.delete_object(id=question_id)

    # if not result:
    #     raise DatabaseErrorException(
    #         detail='Не удалось удалить запись из базы данных.'
    #     )
    return result
