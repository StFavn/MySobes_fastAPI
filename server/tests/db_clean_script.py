from sqlalchemy.ext.asyncio import create_async_engine
from app.database.base_model import Base
import asyncio

from app.modules.topics.models import TopicModel
from app.modules.questions.models import QuestionModel

TEST_DB_URL = 'sqlite+aiosqlite:///./questionsList_test.db'
engine = create_async_engine(TEST_DB_URL)

async def drop_and_create_db():
    async with engine.begin() as conn:
        print("Tables in metadata before drop:", Base.metadata.tables.keys())

        await conn.run_sync(Base.metadata.drop_all)
        print("Tables in metadata was dropped.")
        
        await conn.run_sync(Base.metadata.create_all)
        print("Tables in metadata after create:", Base.metadata.tables.keys())

if __name__ == "__main__":
    asyncio.run(drop_and_create_db())