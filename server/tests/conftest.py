import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from typing import AsyncIterator

from app.main import app
from app.config import settings

@pytest_asyncio.fixture(scope="function", autouse=True)
async def client() -> AsyncIterator[AsyncClient]:
    if settings.MODE != 'TEST':
        raise ValueError(
            "Тестирование необходимо запускать в тестовой среде. "
            "Для запуска тестов введите команду MODE=TEST pytest"
        )
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
