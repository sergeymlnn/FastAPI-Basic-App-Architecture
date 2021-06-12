import asyncio

import pytest
from httpx import AsyncClient

from app.main import app
from app.settings import settings


@pytest.fixture(scope="module")
async def client():
    """"""
    async with AsyncClient(app=app, base_url=settings.api_url) as client:
        yield client


@pytest.fixture(scope="module")
def event_loop():
    """"""
    loop = asyncio.get_event_loop()
    yield loop
