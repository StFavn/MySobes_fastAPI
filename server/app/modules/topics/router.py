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

from .dao import TopicDAO
from .schemas import STopicCreate, STopicRead, STopicTreeRead, STopicUpdate

router = APIRouter(
    prefix='/topics',
    tags=['topics']
)


@router.post('', response_model=STopicRead)
async def create_topic(data: STopicCreate): # user: UserModel = Depends(current_superuser
    """Добавление новой темы."""

    # topic_exists = await TopicDAO.get_object(
    #     name=data.name
    #     parent_id=data.parent_id
    # )
    # if topic_exists:
    #     raise ObjectAlreadyExistsException
    
    new_topic = await TopicDAO.add_object(**data.model_dump())
    # if not new_topic:
    #     raise DatabaseErrorException(
    #         detail='Не удалось добавить запись в базу данных.'
    #     )
    return new_topic


@router.get('/{topic_id}', response_model=STopicTreeRead)
async def get_topic_tree(topic_id: int):
    """Возвращение темы по id."""

    topic = await TopicDAO.get_topic_tree(id=topic_id)
    # if not topic:
    #     raise NotFoundException
    return topic


@router.get('', response_model=List[STopicTreeRead])
async def get_topics_tree():
    """Возвращение списка всех тем в виде дерева."""

    topics = await TopicDAO.get_all_topics_tree()
    # if not topics:
    #     raise NotFoundException
    return topics


@router.patch('/{topic_id}', response_model=STopicRead)
async def update_topic( # user: UserModel = Depends(current_superuser
    topic_id: int,
    update_data: STopicUpdate
):
    """Обновление данных темы."""

    topic = await TopicDAO.update_object(
        update_data=update_data, id=topic_id
    )

    # if not topic:
    #     raise DatabaseErrorException(detail='Не удалось обновить данные.')
    return topic


@router.delete('/{topic_id}')
async def delete_topic(topic_id: int): # user: UserModel = Depends(current_superuser)
    """Удаление темы."""

    result = await TopicDAO.delete_object(id=topic_id)

    # if not result:
    #     raise DatabaseErrorException(
    #         detail='Не удалось удалить запись из базы данных.'
    #     )
    return result
