import re
from typing import List, Union, Dict
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.uix.scrollview import ScrollView

from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR
from lib.coin import Coin
from lib.update import Update
from lib.language import language, Text
from lib.currency import currency, Currency

DELETE_COLOR = get_color_from_hex("#FF0101e6")
ERROR_COLOR = get_color_from_hex("##c91010F6")
SHEET_CHOSEN = get_color_from_hex("#00ff4cF4")
WHITE = get_color_from_hex("#F9F6EEF6")
NAME_OK = get_color_from_hex("#0e9c17")


class ModifyCoin(BoxLayout):
    def __init__(self, scrollapp, popup:Popup, coin:Coin):
        super(ModifyCoin, self).__init__()
        self.scrollapp = scrollapp
        self.popup = popup
        self.coin = coin
        self.orientation = "vertical"
        self.opacity = 0.8
        self.spacing = 5
        self.workbook = Update().try_load_workbook()
        self.coin_name_input = TextInput(text=self.coin.name, size_hint=(1, 0.3))
        self.worksheet_input:str = ""
        self.cell_input = TextInput(text=self.coin.cell, size_hint=(1, 0.3))
        self.scroll_sheets = ScrollView()
        self.sheets_widget = BoxLayout(orientation='vertical', size_hint_y=None, spacing=2)
        self.sheets_widget.bind(minimum_height=self.sheets_widget.setter('height'))
        self.scroll_sheets.add_widget(self.sheets_widget)
        self.sheets = self.workbook.sheetnames
        self.sheets.remove('data')
        for sheet in self.sheets:
            sheet_button = Button(text=sheet, background_color=UNPRESSED_COLOR, size_hint_y = None, height = 35, on_release=self.chosen_sheet)
            if self.coin.worksheet == sheet:
                self.worksheet_input = sheet
                sheet_button.background_color = SHEET_CHOSEN
            self.sheets_widget.add_widget(sheet_button)
        self.add_widget(self.coin_name_input)
        self.add_widget(self.scroll_sheets)
        self.add_widget(self.cell_input)
        buttons = BoxLayout(orientation='horizontal', size_hint=(1, 0.4))
        self.add_widget(buttons)
        buttons.add_widget(Button(text=language.get_text(Text.MODIFY.value), on_release=self.modify, size_hint=(0.5, 1),
                               background_color=UNPRESSED_COLOR))
        buttons.add_widget(Button(text=language.get_text(Text.DELETE.value), on_release=self.delete, size_hint=(0.5, 1),
                               background_color=DELETE_COLOR))

    def chosen_sheet(self, dt):
        if dt.background_color == UNPRESSED_COLOR:
            for sheet in self.sheets_widget.children:
                sheet.color = WHITE
            dt.background_color = SHEET_CHOSEN
            self.worksheet_input = dt.text
            for sheet in self.sheets_widget.children:
                if dt is not sheet:
                    sheet.background_color = UNPRESSED_COLOR
        else:
            for sheet in self.sheets_widget.children:
                sheet.color = WHITE
            self.worksheet_input = ""
            dt.background_color = UNPRESSED_COLOR

        
    def modify(self, dt):
        dt.background_color=PRESSED_COLOR
    
        data = self.workbook['data']
        price = self.check_input_data()
        if price[0]:
            data = self.workbook['data']
            data.cell(row=1, column=self.coin.id).value = self.coin_name_input.text.upper()
            data.cell(row=2, column=self.coin.id).value = self.worksheet_input
            data.cell(row=3, column=self.coin.id).value = self.cell_input.text.upper()
            self.workbook.save(language.read_file()['path_to_xlsx'])
            for coin in self.scrollapp.coins_tab:
                if coin.id == self.coin.id:
                    coin.name = self.coin_name_input.text.upper()
                    coin.worksheet = self.worksheet_input
                    coin.cell = self.cell_input.text.upper()
                    coin.price_usd = price[1][Currency.USD]
                    coin.price_pln = price[1][Currency.PLN]
                    break
            self.scrollapp.initialize_coins()
            self.popup.dismiss()

    def delete(self, dt):
        dt.background_color=PRESSED_COLOR

        data = self.workbook['data']
        data.cell(row=1, column=self.coin.id).value = "-"
        data.cell(row=2, column=self.coin.id).value = ""
        data.cell(row=3, column=self.coin.id).value = ""
        self.workbook.save(language.read_file()['path_to_xlsx'])
        for coin in self.scrollapp.coins_tab:
                if coin.id == self.coin.id:
                    self.scrollapp.coins_tab.remove(coin)
                    break
        self.scrollapp.initialize_coins()
        self.scrollapp.coins.height = self.scrollapp.SPACING + self.scrollapp.COIN_HEIGHT * len(self.scrollapp.coins_tab)
        self.popup.dismiss()

    def check_input_data(self) -> List[Union[bool, Dict[Currency, str]]]:
        if self.coin_name_input.text != self.coin.name:
            test_price: Dict[Currency, str] = Update().get_token_price(self.coin_name_input.text)
        else:
            test_price = {Currency.USD: self.coin.price_usd, Currency.PLN: self.coin.price_pln}

        name_ok: bool = False
        sheet_ok: bool = False
        cell_ok: bool = False
        ##############################################
        if test_price != None:
            self.coin_name_input.foreground_color = NAME_OK
            name_ok = True
        else:
            self.coin_name_input.foreground_color = ERROR_COLOR
        ##############################################
        if 'data' not in self.workbook.sheetnames:
            self.workbook.create_sheet('data')
            hidden = self.workbook['data']
            hidden.sheet_state = 'hidden'
            self.workbook.save(language.read_file()['path_to_xlsx'])
        if self.worksheet_input != "":
            sheet_ok = True
        else:
            for sheet in self.sheets_widget.children:
                sheet.color = ERROR_COLOR
        ##############################################
        cell_pattern = r'^[A-Za-z]\d+$'
        if re.match(cell_pattern, self.cell_input.text):
            self.cell_input.foreground_color = PRESSED_COLOR
            cell_ok = True
        else:
            self.cell_input.foreground_color = ERROR_COLOR
        ##############################################
        return [name_ok & sheet_ok & cell_ok, test_price]
