from kivy.uix.button import Button
from kivy.uix.popup import Popup

from widgets.menu import UNPRESSED_COLOR
from widgets.modify_coin import ModifyCoin
from lib.asset import Asset
from lib.language import language, Text
from lib.currency import currency, Currency


class CoinButton(Button):
    SPACING:int = 2
    COIN_HEIGHT:int = 40

    def __init__(self, scrollapp, coin:Asset):
        super().__init__()
        self.currency_logo = ""
        self.coin_price = ""
        match coin.chosen_currency:
            case Currency.USD:
                self.currency_logo = "$"
                self.coin_price = coin.price_usd
            case Currency.PLN:
                self.currency_logo = "zł"
                self.coin_price = coin.price_pln
            case Currency.GBP:
                self.currency_logo = "£"
                self.coin_price = coin.price_gbp
            case Currency.EUR:
                self.currency_logo = "€"
                self.coin_price = coin.price_eur
        
        self.coin = coin
        self.scrollapp = scrollapp
        self.font_size = 16
        self.text_size = (None, None)
        self.text: str = f"{self.coin.name:<115}{self.currency_logo} {self.coin_price}"
        self.worksheet:str = self.coin.worksheet
        self.halign = 'left'
        self.cell:str = self.coin.cell
        self.height:int = self.COIN_HEIGHT
        self.background_color=UNPRESSED_COLOR

    def on_press(self):
        modify_coin_menu = Popup(size_hint=(None, None), size=(400, 400), auto_dismiss=True, 
                                 title=f"{language.get_text(Text.EDIT_COIN.value)} {self.coin.name}", background_color = UNPRESSED_COLOR)
        add_menu = ModifyCoin(scrollapp=self.scrollapp, popup=modify_coin_menu, coin=self.coin)
        modify_coin_menu.content = add_menu
        modify_coin_menu.open(animation=True)
