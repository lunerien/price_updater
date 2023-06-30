from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from typing import List

from widgets.coin_button import CoinButton
from lib.coin import Coin
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR


class ScrollApp(ScrollView):
    SPACING = 2
    COIN_HEIGHT = 40

    def __init__(self):
        super().__init__()
        self.coins_tab:List[Coin] = []
        self.coins = GridLayout(cols=1, spacing=self.SPACING, size_hint_y=None)
        self.add_widget(self.coins)
        self.initialize_coins()
        self.coins.height = self.SPACING + self.COIN_HEIGHT * len(self.coins_tab)
        self.bar_color = PRESSED_COLOR
        self.bar_width=5

    def initialize_coins(self):
        self.coins.clear_widgets()
        for coin in self.coins_tab:
            coin_button = CoinButton(scrollapp=self, coin=coin)
            self.coins.add_widget(coin_button)

