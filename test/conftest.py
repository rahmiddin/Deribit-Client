import aiohttp
import pytest

from src.client.client import get_ticker


@pytest.mark.asyncio
async def test_get_ticker():
    session = aiohttp.ClientSession()

    symbols = ['BTC', 'ETH']
    for symbol in symbols:
        ticker = await get_ticker(session, symbol)

        assert ticker
