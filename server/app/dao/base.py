from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import async_session_maker
from app.logger import logger

class BaseDAO:
    """Класс для работы с объектами БД."""

    model = None

    @classmethod
    async def get_object(cls, **kwargs):
        """Возвращение одного объекта модели из БД."""
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns).filter_by(**kwargs)
                result = await session.execute(query)
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        return result.mappings().one_or_none()
    
    @classmethod
    async def get_all_objects(cls, **kwargs):
        """Возвращение всех объектов модели из БД."""
        try:
            async with async_session_maker() as session:
                query = (select(cls.model.__table__.columns)
                         .filter_by(**kwargs)
                         .order_by(cls.model.id))
                result = await session.execute(query)
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        return result.mappings().all()
    
    @classmethod
    async def add_object(cls, **kwargs):
        """Добавление объекта в БД."""
        try:
            async with async_session_maker() as session:
                new_object = cls.model(**kwargs)
                session.add(new_object)
                await session.commit()

                return new_object
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
    
    @classmethod
    async def update_object(cls, update_data, **kwargs):
        """Обновление данных объекта в БД."""
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(**kwargs)
                result = await session.execute(query)
                result = result.scalar_one_or_none()
                new_data = update_data.model_dump(exclude_unset=True)

                for key, value in new_data.items():
                    setattr(result, key, value)
                session.add(result)
                await session.commit()
                await session.refresh(result)
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        return result
    
    @classmethod
    async def delete_object(cls, **kwargs):
        """Удаление объекта из БД."""
        try:
            async with async_session_maker() as session:
                query = select(cls.model).filter_by(**kwargs)
                result = await session.execute(query)
                result = result.scalar_one_or_none()
                await session.delete(result)
                await session.commit()
        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        return 'Удаление успешно завершено.'
    
    @classmethod
    async def delete_all_objects(cls, **kwargs):
        """Удаление всех объектов из БД."""
        try:
            async with async_session_maker() as session:
                async with session.begin():
                    query = select(cls.model).filter_by(**kwargs)
                    results = await session.execute(query)
                    results = results.scalars().all()

                    for result in results:
                        await session.delete(result)

        except (SQLAlchemyError, Exception) as error:
            message = f'An error has occurred: {error}'
            logger.error(
                message,
                extra={'Database table': cls.model.__tablename__},
                exc_info=True
            )
            return None
        return 'Удаление всех объектов успешно завершено.'