from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.database.models import Model

DB_CONFIG = "sqlite+aiosqlite:///questionsList.db"

engine = create_async_engine(DB_CONFIG)
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)