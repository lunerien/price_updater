from typing import Any
from enum import Enum
import json


class Languages(Enum):
    EN = "EN"
    PL = "PL"
    DE = "DE"


class Text(Enum):
    UPDATE = "update"
    EDIT_COIN = "edit_asset"
    MODIFY = "modify"
    DELETE = "delete"
    COIN_NAME = "asset"
    WORKSHEET_NAME = "worksheet_name"
    CELL = "cell"
    ADD = "add"
    ADD_NEW_COIN = "add_new_asset"
    CHANGE_XLSX_WORKBOOK = "change_xlsx_workbook"
    PATH_TO_XLSX = "path_to_xlsx"
    SEARCH = "search"
    EMPTY_LIST_TEXT = "your_assets_will_be_here"
    LOADING_LIST_TEXT = "please_wait"
    PLEASE_SELECT_WORKBOOK = "please_select_workbook"
    FETCH_ERROR_TITLE = "fetch_error_title"
    FETCH_ERROR_MSG = "fetch_error_msg"
    CONNECTION_LOST = "connection_lost"
    DATA_SAVING_SUCCESSFUL = "data_saving_successful"
    DATA_SAVING_FAILED = "data_saving_failed"
    REFRESH_DATA = "refresh_data"
    CHANGE_LANGUAGE = "change_language"


class Language:
    def __init__(self) -> None:
        self.language_file: Any = self.read_file()

    def get_current_language(self) -> str:
        return self.language_file["chosen_language"]

    def get_text(self, word: str) -> str:
        return self.language_file[self.get_current_language()][word]

    def read_file(self) -> Any:
        with open("data.json", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def change_language(self, new_language: Languages) -> None:
        with open("data.json", "r+", encoding="utf-8") as file:
            data: Any = json.load(file)
            data["chosen_language"] = new_language.value
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        self.language_file = self.read_file()


language = Language()
