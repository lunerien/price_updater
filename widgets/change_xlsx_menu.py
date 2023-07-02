from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from tkinter.filedialog import askopenfilename
import json
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException

from widgets.scroll_app import ScrollApp
from lib.language import language, Text
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR


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
        self.open_file_button = Button(text=language.get_text(Text.SEARCH.value), on_release= self.choose_path, size_hint=(0.15, 0.7), background_color=UNPRESSED_COLOR)
        self.input_and_ask_open_file.add_widget(self.open_file_button)
        buttons = BoxLayout(orientation='horizontal')
        self.add_widget(buttons)
        buttons.add_widget(Button(text=language.get_text(Text.MODIFY.value), on_release=self.add_path, size_hint=(0.4, 0.7),
                               background_color=UNPRESSED_COLOR))
        self.choose_path(1)

    def add_path(self, dt):
        dt.background_color=PRESSED_COLOR
        try:
            wb = load_workbook(self.path_xlsx_input.text)
            with open('data.json', 'r+') as file:
                data = json.load(file)
                data['path_to_xlsx'] = self.path_xlsx_input.text
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
            from main import main_app
            main_app.restart()
            self.popup.dismiss()
        except InvalidFileException:
            print("we need xlsx file!")
        except KeyError:
            print("please check xlsx format file!")

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
        
