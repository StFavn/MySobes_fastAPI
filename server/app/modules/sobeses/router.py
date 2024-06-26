from typing import List

from fastapi import APIRouter

from app.exceptions import (
    DatabaseErrorException,
    NotFoundException
)

from .dao import SobesDAO
from .schemas import SSobesCreate, SSobesRead, SSobesUpdate

router = APIRouter(
    prefix='/sobeses',
    tags=['sobeses']
)


@router.post('', response_model=SSobesRead)
async def create_sobes(data: SSobesCreate):
    """Добавление нового собеса."""
    
    new_sobes = await SobesDAO.create_sobes(**data.model_dump())
    if not new_sobes:
        raise DatabaseErrorException(
            detail='Не удалось добавить запись в базу данных.'
        )
    return new_sobes


@router.post('/{sobes_id}/recalculate_score', response_model=SSobesRead)
async def recalculate_sobes(sobes_id: int): 
    """Перерасчет average_score и duration для собеса."""
    
    recalculate_sobes = await SobesDAO.recalculate_score(sobes_id=sobes_id)
    if not recalculate_sobes:
        raise DatabaseErrorException(
            detail='Не удалось добавить запись в базу данных.'
        )
    return recalculate_sobes


@router.get('/{sobes_id}', response_model=SSobesRead)
async def get_sobes(sobes_id: int):
    """Возвращение собеса по id."""

    sobes = await SobesDAO.get_sobes_by_id(id=sobes_id)
    if not sobes:
        raise NotFoundException
    return sobes


@router.get('', response_model=List[SSobesRead])
async def get_sobeses():
    """Возвращение списка всех собесов."""

    sobeses = await SobesDAO.get_all_sobeses()
    if not sobeses:
        raise NotFoundException
    return sobeses


@router.patch('/{sobes_id}', response_model=SSobesRead)
async def update_sobes( # user: UserModel = Depends(current_superuser
    sobes_id: int,
    update_data: SSobesUpdate
):
    """Обновление данных вопроса."""

    update_sobes = await SobesDAO.update_object(
        update_data=update_data, id=sobes_id
    )

    if not update_sobes:
        raise DatabaseErrorException(detail='Не удалось обновить данные.')
    
    sobes = await SobesDAO.get_sobes_by_id(id=sobes_id)
    if not sobes:
        raise NotFoundException
    return sobes


@router.delete('/{sobes_id}')
async def delete_sobes(sobes_id: int): # user: UserModel = Depends(current_superuser)
    """Удаление вопроса."""

    result = await SobesDAO.delete_object(id=sobes_id)

    if not result:
        raise DatabaseErrorException(
            detail='Не удалось удалить запись из базы данных.'
        )
    return result
