import pytest


@pytest.mark.asyncio
async def test_main(client):
    """"""
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") == "Hello, World!"
