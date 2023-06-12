from sqlalchemy import Column, Integer, String

from src.database import Base


class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    price = Column(Integer)
    time = Column(Integer)
