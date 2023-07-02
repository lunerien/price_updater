from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from openpyxl import load_workbook

from widgets.scroll_app import ScrollApp
from lib.coin import Coin
from lib.language import language, Text
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR

class AddMenu(BoxLayout):
    def __init__(self, scrollApp:ScrollApp, popup:Popup, **kwargs):
        super(AddMenu, self).__init__(**kwargs)
        self.scrollapp = scrollApp
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.coin_name_input = TextInput(text=language.get_text(Text.COIN_NAME.value), size_hint=(1, 0.5), multiline=False)
        self.worksheet_name_input = TextInput(text=language.get_text(Text.WORKSHEET_NAME.value), size_hint=(1, 0.5), multiline=False)
        self.cell_input = TextInput(text=language.get_text(Text.CELL.value), size_hint=(1, 0.5), multiline=False)
        self.add_widget(self.coin_name_input)
        self.add_widget(self.worksheet_name_input)
        self.add_widget(self.cell_input)
        buttons = BoxLayout(orientation='horizontal')
        self.add_widget(buttons)
        buttons.add_widget(Button(text=language.get_text(Text.ADD.value), on_release=self.add_this_coin, size_hint=(0.4, 0.7),
                               background_color=UNPRESSED_COLOR))

    def add_this_coin(self, dt):
        dt.background_color=PRESSED_COLOR

        workbook = load_workbook(language.read_file()['path_to_xlsx'])
        if 'data' in workbook.sheetnames:
            None
        else:
            workbook.create_sheet('data')
            hidden = workbook['data']
            hidden.sheet_state = 'hidden'
            workbook.save(language.read_file()['path_to_xlsx'])
        
        data = workbook['data']
        i = 1
        while data.cell(row=1, column=i).value != "-" and data.cell(row=1, column=i).value != None:
            i += 1
        
        data.cell(row=1, column=i).value = self.coin_name_input.text
        data.cell(row=2, column=i).value = self.worksheet_name_input.text
        data.cell(row=3, column=i).value = self.cell_input.text
        workbook.save(language.read_file()['path_to_xlsx'])
        self.scrollapp.initialize_coins()
        self.scrollapp.coins.height = ScrollApp.SPACING + ScrollApp.COIN_HEIGHT * len(self.scrollapp.coins_tab)
        self.popup.dismiss()
