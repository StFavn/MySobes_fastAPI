from typing import List
from fastapi import APIRouter

from app.exceptions import (
    DatabaseErrorException,
    NotFoundException
)

from .dao import SobesQuestionDAO
from .schemas import SSobesQuestionRead, SSobesQuestionUpdate

router = APIRouter(
    prefix='/sobes_questions',
    tags=['sobes_questions']
)



@router.get('/{sobes_question_id}', response_model=SSobesQuestionRead)
async def get_sobes_question(sobes_question_id: int):
    """Возвращение sobes_question по id."""

    sobes_question = await SobesQuestionDAO.get_object(id=sobes_question_id)
    if not sobes_question:
        raise NotFoundException
    return sobes_question


@router.get('/sobes/{sobes_id}', response_model=List[SSobesQuestionRead])
async def get_sobes_questions(sobes_id: int):
    """Возвращение списка всех sobes_questions по sobes_id."""

    sobes_questions = await SobesQuestionDAO.get_all_objects(sobes_id=sobes_id)
    if not sobes_questions:
        raise NotFoundException
    return sobes_questions


@router.patch('/{sobes_question_id}', response_model=SSobesQuestionRead)
async def update_sobes_question( # user: UserModel = Depends(current_superuser
    sobes_question_id: int,
    update_data: SSobesQuestionUpdate
):
    """Обновление данных sobes_question."""

    sobes_question = await SobesQuestionDAO.update_object(
        update_data=update_data, id=sobes_question_id
    )

    if not sobes_question:
        raise DatabaseErrorException(detail='Не удалось обновить данные.')
    return sobes_question
