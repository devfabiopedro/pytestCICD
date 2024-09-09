import asyncio
import pytest


#função assíncrona para testar
async def fetch_data():
        await asyncio.sleep(2)
        return {'data':'algum dado...'}


# Teste unitário e assíncrono

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == {'data':'algum dado...'}
