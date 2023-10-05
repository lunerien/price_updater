from kivymd.uix.button import MDRaisedButton
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles

from widgets.modify_coin import ModifyCoin
from lib.asset import Asset
from lib.language import language, Text
from lib.currency import Currency
from lib.config import *


class CoinButton(MDRaisedButton):
    def __init__(self, scrollapp, coin: Asset):
        super().__init__()
        self.SPACING: int = 2
        self.COIN_HEIGHT: int = 40
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
        self.size_hint = (1, self.COIN_HEIGHT)
        self.coin = coin
        self.scrollapp = scrollapp
        self.font_size = 18
        self.text_size = (None, None)
        self.worksheet: str = self.coin.worksheet
        self.halign = "left"
        self.cell: str = self.coin.cell
        self.font_name = font_config
        self.height: int = self.COIN_HEIGHT
        self.md_bg_color = COLOR_BUTTON

        self.coin_frame = MDBoxLayout(orientation="horizontal")
        self.name_label = MDLabel(
            text=self.coin.name,
            halign="left",
            theme_text_color="Secondary",
            font_style=theme_font_styles[5],
        )
        self.price_label = MDLabel(
            text=f"{self.currency_logo} {self.coin_price}",
            halign="right",
            theme_text_color="Secondary",
            font_style=theme_font_styles[5],
        )
        self.coin_frame.add_widget(self.name_label)
        self.coin_frame.add_widget(self.price_label)
        self.add_widget(self.coin_frame)

    def on_press(self):
        modify_coin_menu = Popup(
            title_color=COLOR_ORANGE_THEME,
            overlay_color=COLOR_BEHIND_WINDOW,
            separator_color=COLOR_ORANGE_THEME,
            size_hint=(None, None),
            size=(400, 400),
            auto_dismiss=True,
            title=f"{language.get_text(Text.EDIT_COIN.value)} {self.coin.name}",
            background_color=COLOR_WINDOW,
            title_font=font_config,
        )
        add_menu = ModifyCoin(
            scrollapp=self.scrollapp, popup=modify_coin_menu, coin=self.coin
        )
        modify_coin_menu.content = add_menu
        modify_coin_menu.open(animation=True)
