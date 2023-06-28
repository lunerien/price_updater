from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from widgets.coin_button import CoinButton
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR


class ScrollApp(ScrollView):
    AMOUNT_OF_COINS = 0
    SPACING = 2

    def __init__(self):
        super().__init__()
        self.coins = GridLayout(cols=1, spacing=self.SPACING, size_hint_y=None)
        self.add_widget(self.coins)
        self.coins_counter = 0
        self.initialize_coins()
        self.coins.height = self.SPACING + CoinButton.COIN_HEIGHT * self.AMOUNT_OF_COINS
        self.bar_color = PRESSED_COLOR
        self.bar_width=5
        

    def initialize_coins(self):
        for _ in range(self.AMOUNT_OF_COINS):
            coin_button = CoinButton(scrollapp=self)
            self.coins.add_widget(coin_button)
            self.coins_counter += 1
