from sqlalchemy import select

from src.client.models import Currency
from src.dao.base import BaseDAO
from src.database import async_session_maker


class ClientDAO(BaseDAO):
    model = Currency

    @classmethod
    async def find_last_price(cls, ticker):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(ticker=ticker)
            result = await session.execute(query)
            return result.mappings().all()[-1]['price']

    @classmethod
    async def find_price_by_datetime(cls, ticker: str, date: int):
        async with async_session_maker() as session:
            query = select(cls.model.price).filter(
                Currency.time == date, Currency.ticker == ticker).order_by(Currency.time.desc())
            result = await session.execute(query)
            return result.mappings().all()

