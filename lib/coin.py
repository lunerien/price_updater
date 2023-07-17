from lib.update import Update

class Coin:
    def __init__(self, id:int, name:str, worksheet:str, cell:str):
        self.id:int = id
        self.name:str = name
        self.worksheet:str = worksheet
        self.cell:str = cell
        self.price: str = ""


    
