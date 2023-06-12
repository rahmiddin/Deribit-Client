from dataclasses import dataclass


@dataclass
class SCurrencyAll:
    ticker: str
    price: int
    time: int
