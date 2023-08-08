from typing import Dict

from lib.currency import Currency

class Coin:
    def __init__(self, id:int, name:str, worksheet:str, cell:str, price:Dict[Currency, str]):
        self.id:int = id
        self.name:str = name
        self.worksheet:str = worksheet
        self.cell:str = cell
        self.price_usd: str = price[Currency.USD]
        self.price_pln: str = price[Currency.PLN]

