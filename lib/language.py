from enum import Enum
import json


class Languages(Enum):
    EN = "EN"
    PL = "PL"


class Text(Enum):
    UPDATE = "update"
    EDIT_COIN = "edit_coin"
    MODIFY = "modify"
    DELETE = "delete"
    COIN_NAME = "coin_name"
    WORKSHEET_NAME = "worksheet_name"
    CELL = "cell"
    ADD = "add"
    ADD_NEW_COIN = "add_new_coin"
    CHANGE_XLSX_WORKBOOK = "change_xlsx_workbook"
    PATH_TO_XLSX = "path_to_xlsx"
    SEARCH = "search"


class Language:
    def __init__(self):
        self.language_file = self.read_file()

    def get_current_language(self) -> str:
        return self.language_file['chosen_language']
    
    def get_text(self, word:str):
        return self.language_file[self.get_current_language()][word]

    def read_file(self) -> str:
        file = open('data.json')
        data = json.load(file)
        return data
    
    def change_language(self, new_language:Languages):
        with open('data.json', 'r+') as file:
            data = json.load(file)
            data['chosen_language'] = new_language.value
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        self.language_file = self.read_file()
        from main import main_app
        main_app.restart()


language = Language()
