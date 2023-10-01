from kivy.uix.button import Button
from kivy.uix.popup import Popup

from widgets.modify_coin import ModifyCoin
from lib.asset import Asset
from lib.language import language, Text
from lib.currency import Currency
from lib.config import *


class CoinButton(Button):
    SPACING: int = 2
    COIN_HEIGHT: int = 40

    def __init__(self, scrollapp, coin: Asset):
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
        self.font_size = 17
        self.text_size = (None, None)
        if self.coin_price == "0,0":
            self.color = ERROR_COLOR
        self.text: str = f"{self.coin.name:<115}{self.currency_logo} {self.coin_price}"
        self.worksheet: str = self.coin.worksheet
        self.halign = "left"
        self.cell: str = self.coin.cell
        self.font_name = font_config
        self.height: int = self.COIN_HEIGHT
        self.background_color = ASSET_BUTTON
        self.color = TOP_BAR_COLOR

    def on_press(self):
        modify_coin_menu = Popup(
            overlay_color=BEHIND_WINDOW,
            separator_color = WINDOW,
            size_hint=(None, None),
            size=(400, 400),
            auto_dismiss=True,
            title=f"{language.get_text(Text.EDIT_COIN.value)} {self.coin.name}",
            background_color=WINDOW,
            title_font=font_config
        )
        add_menu = ModifyCoin(
            scrollapp=self.scrollapp, popup=modify_coin_menu, coin=self.coin
        )
        modify_coin_menu.content = add_menu
        modify_coin_menu.open(animation=True)
