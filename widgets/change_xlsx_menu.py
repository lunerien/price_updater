import json
from typing import List
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from tkinter.filedialog import askopenfilename
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException

from widgets.scroll_app import ScrollApp
from lib.language import language, Text
from lib.asset import Asset
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR

ERROR_COLOR = get_color_from_hex("##c91010F6")

class ChangeXlsxMenu(BoxLayout):
    def __init__(self, scrollApp:ScrollApp, popup:Popup, **kwargs):
        super(ChangeXlsxMenu, self).__init__(**kwargs)
        self.scrollapp = scrollApp
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.input_and_ask_open_file = BoxLayout(orientation="horizontal")
        self.add_widget(self.input_and_ask_open_file)
        self.path_xlsx_input = TextInput(text=self.load_current_path(), size_hint=(0.85, 0.7), multiline=False)
        self.input_and_ask_open_file.add_widget(self.path_xlsx_input)
        self.open_file_button = Button(text=language.get_text(Text.SEARCH.value), 
                                       on_release= self.choose_path, size_hint=(0.15, 0.7), background_color=UNPRESSED_COLOR)
        self.input_and_ask_open_file.add_widget(self.open_file_button)
        buttons = BoxLayout(orientation='horizontal')
        self.add_widget(buttons)
        buttons.add_widget(Button(text=language.get_text(Text.MODIFY.value), on_release=self.add_path, size_hint=(0.4, 0.9),
                               background_color=UNPRESSED_COLOR))
        # self.choose_path(1)

    def add_path(self, dt):
        dt.background_color=PRESSED_COLOR
        if self.path_xlsx_input.text != self.load_current_path():
            try:
                wb = load_workbook(self.path_xlsx_input.text)
                with open('data.json', 'r+') as file:
                    data = json.load(file)
                    data['path_to_xlsx'] = self.path_xlsx_input.text
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                self.popup.dismiss()
                self.scrollapp.coins_tab:List[Asset] = self.scrollapp.get_coins_from_xlsx()
                self.scrollapp.initialize_coins()
            except InvalidFileException:
                self.path_xlsx_input.foreground_color = ERROR_COLOR
                print("we need xlsx file!")
            except KeyError:
                self.path_xlsx_input.foreground_color = ERROR_COLOR
                print("please check xlsx format file!")
            except FileNotFoundError:
                self.path_xlsx_input.foreground_color = ERROR_COLOR
                print("file missing :D")
        else:
            self.popup.dismiss()

    def load_current_path(self) -> str:
        file = open('data.json')
        data = json.load(file)
        path = data["path_to_xlsx"]
        if path == "":
            return language.get_text(Text.PATH_TO_XLSX.value)
        else:
            return data["path_to_xlsx"]
  
    def choose_path(self, dt):
        path = askopenfilename(title=language.get_text(Text.PATH_TO_XLSX.value))
        if path != "":
            self.path_xlsx_input.text = path
        
