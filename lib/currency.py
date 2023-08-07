from enum import Enum
import json


class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class CCurrency:
    def __init__(self):
        self.data_file = self.read_file()

    def get_current_currency(self) -> str:
        return self.data_file['chosen_currency']

    def read_file(self) -> str:
        file = open('data.json')
        data = json.load(file)
        return data
    
    def change_currency(self, new_currency:Currency):
        with open('data.json', 'r+') as file:
            data = json.load(file)
            data['chosen_currency'] = new_currency.value
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        self.language_file = self.read_file()


currency = CCurrency()