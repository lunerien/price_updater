from kivy.uix.button import Button
from kivy.uix.popup import Popup

from widgets.menu import UNPRESSED_COLOR
from widgets.modify_coin import ModifyCoin
from lib.coin import Coin
from lib.language import language, Text


class CoinButton(Button):
    SPACING:int = 2
    COIN_HEIGHT:int = 40

    def __init__(self, scrollapp, coin:Coin):
        super().__init__()
        self.coin = coin
        self.scrollapp = scrollapp
        self.font_size = 16
        self.text_size = (None, None)
        self.text: str = f"{self.coin.name:<115}${self.coin.price}"
        self.worksheet:str = self.coin.worksheet
        self.halign = 'left'
        self.cell:str = self.coin.cell
        self.height:int = self.COIN_HEIGHT
        self.background_color=UNPRESSED_COLOR

    def on_release(self):
        modify_coin_menu = Popup(size_hint=(None, None), size=(400, 300), auto_dismiss=True, 
                                 title=language.get_text(Text.EDIT_COIN.value), background_color = UNPRESSED_COLOR)
        add_menu = ModifyCoin(scrollapp=self.scrollapp, popup=modify_coin_menu, coin=self.coin)
        modify_coin_menu.content = add_menu
        modify_coin_menu.open(animation=True)
