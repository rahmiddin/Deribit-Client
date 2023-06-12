import asyncio
import aiohttp
import time

from src.client.dao import ClientDAO


async def get_ticker(session, symbol):
    url = f'https://www.deribit.com/api/v2/public/ticker?instrument_name={symbol}-PERPETUAL'
    async with session.get(url) as response:
        data = await response.json()
        timestamp = int(time.time())
        ticker = {
            'ticker': symbol,
            'price': data['result']['last_price'],
            'time': timestamp
        }
        return ticker


async def main():
    symbols = ['BTC', 'ETH']
    async with aiohttp.ClientSession() as session:
        while True:
            for symbol in symbols:
                data = await get_ticker(session, symbol)
                print(data)
                await ClientDAO.insert_data(ticker=data['ticker'],
                                            price=data['price'],
                                            time=data['time'])
            # Wait for 1 minute
            await asyncio.sleep(60)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())