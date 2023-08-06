import asyncio
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from typing import List
from openpyxl import load_workbook

from widgets.coin_button import CoinButton
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR
from lib.coin import Coin
from lib.language import language, Text
from lib.update import Update


class ScrollApp(ScrollView):
    SPACING = 2
    COIN_HEIGHT = 40

    def __init__(self):
        super().__init__()
        self.coins_tab:List[Coin] = self.get_coins_from_xlsx()
        self.coins = GridLayout(cols=1, spacing=self.SPACING, size_hint_y=None)
        self.empty_list: Label = Label(text=language.get_text(Text.EMPTY_LIST_TEXT.value))
        self.add_widget(self.coins)
        self.initialize_coins()
        self.coins.height = self.SPACING + self.COIN_HEIGHT * len(self.coins_tab)
        self.bar_color = PRESSED_COLOR
        self.bar_width=5
        
    def initialize_coins(self):
        self.coins.clear_widgets()
        if len(self.coins_tab):
            for coin in self.coins_tab:
                coin_button = CoinButton(scrollapp=self, coin=coin)
                self.coins.add_widget(coin_button)
        else:
            self.coins.add_widget(self.empty_list)
            self.coins.height = self.SPACING + self.COIN_HEIGHT * len(self.coins_tab)

    def get_coins_from_xlsx(self):
        try:
            workbook = load_workbook(language.read_file()['path_to_xlsx'])
        except:
            return []

        if 'data' in workbook.sheetnames:
            None
        else:
            workbook.create_sheet('data')
            hidden = workbook['data']
            hidden.sheet_state = 'hidden'
            workbook.save(language.read_file()['path_to_xlsx'])
        data = workbook['data']

        coins:List[Coin] = []

        i = 1
        while data.cell(row=1, column=i).value != None:
            if data.cell(row=1, column=i).value != "-":
                ticker = data.cell(row=1, column=i).value
                worksheet = data.cell(row=2, column=i).value
                cell = data.cell(row=3, column=i).value
                price = Update().get_token_price(ticker)
                coins.append(Coin(id=i, name=ticker, worksheet=worksheet, cell=cell, price=price))
            i += 1
        return coins

