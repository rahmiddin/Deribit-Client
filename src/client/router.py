from fastapi import APIRouter

from src.client.dao import ClientDAO
from src.client.schemas import SCurrencyAll

router = APIRouter(
    prefix='/currency',
    tags=['Currency']
)


@router.get('/get_all')
async def get_all(ticker: str) -> list[SCurrencyAll]:
    data = await ClientDAO.find_all(ticker=ticker)
    return data


@router.get('/get_last_price')
async def get_all(ticker: str):
    data = await ClientDAO.find_last_price(ticker=ticker)
    return data


@router.get('/get_price_by_date')
async def get_all(ticker: str, date: int):
    data = await ClientDAO.find_price_by_datetime(ticker=ticker, date=date)
    return data
