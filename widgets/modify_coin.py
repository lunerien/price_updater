import re
from typing import List, Union, Dict
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from lib.asset import Asset
from lib.update import Update
from lib.text_input import TextInputC
from lib.button import ButtonC
from lib.language import language, Text
from lib.currency import Currency
from lib.auto_suggestion_text import AutoSuggestionText
from coins_list import coins_list
from lib.config import *


class ModifyCoin(BoxLayout):
    def __init__(self, scrollapp, popup: Popup, coin: Asset):
        super(ModifyCoin, self).__init__()
        self.scrollapp = scrollapp
        self.popup = popup
        self.coin = coin
        self.orientation = "vertical"
        self.opacity = 0.8
        self.spacing = 5
        self.workbook = Update().try_load_workbook()
        self.coin_name_input = AutoSuggestionText(text="", suggestions=coins_list)
        self.worksheet_input: str = ""
        self.cell_input = TextInputC(text=self.coin.cell)
        chosen_currency = self.get_chosen_currency()
        self.checkboxes_currency = BoxLayout(
            orientation="horizontal", size_hint=(1, 0.15)
        )
        self.checkbox_currency_labels = BoxLayout(
            orientation="horizontal", size_hint=(1, 0.07)
        )
        self.checkbox_usd = CheckBox(
            active=True if chosen_currency == Currency.USD else False, color=CHECKBOX
        )
        self.checkbox_usd.bind(active=self.on_checkbox_active)
        self.checkbox_eur = CheckBox(
            active=True if chosen_currency == Currency.EUR else False, color=CHECKBOX
        )
        self.checkbox_eur.bind(active=self.on_checkbox_active)
        self.checkbox_gbp = CheckBox(
            active=True if chosen_currency == Currency.GBP else False, color=CHECKBOX
        )
        self.checkbox_gbp.bind(active=self.on_checkbox_active)
        self.checkbox_pln = CheckBox(
            active=True if chosen_currency == Currency.PLN else False, color=CHECKBOX
        )
        self.checkbox_pln.bind(active=self.on_checkbox_active)
        self.label_usd = Label(text="USD", color=NAME_OK, font_name=font_config)
        self.label_eur = Label(text="EUR", color=NAME_OK, font_name=font_config)
        self.label_gbp = Label(text="GBP", color=NAME_OK, font_name=font_config)
        self.label_pln = Label(text="PLN", color=NAME_OK, font_name=font_config)
        self.checkbox_currency_labels.add_widget(self.label_usd)
        self.checkbox_currency_labels.add_widget(self.label_eur)
        self.checkbox_currency_labels.add_widget(self.label_gbp)
        self.checkbox_currency_labels.add_widget(self.label_pln)
        self.checkboxes_currency.add_widget(self.checkbox_usd)
        self.checkboxes_currency.add_widget(self.checkbox_eur)
        self.checkboxes_currency.add_widget(self.checkbox_gbp)
        self.checkboxes_currency.add_widget(self.checkbox_pln)

        self.scroll_sheets = ScrollView()
        self.sheets_widget = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing=2
        )
        self.sheets_widget.bind(minimum_height=self.sheets_widget.setter("height"))
        self.scroll_sheets.add_widget(self.sheets_widget)
        self.sheets = self.workbook.sheetnames
        self.sheets.remove("data")
        for sheet in self.sheets:
            sheet_button = Button(
                text=sheet,
                background_color=UNPRESSED_COLOR,
                size_hint_y=None,
                height=35,
                on_release=self.chosen_sheet,
                font_name=font_config,
                font_size=17,
                color=WHITE,
            )
            if self.coin.worksheet == sheet:
                self.worksheet_input = sheet
                sheet_button.background_color = SHEET_CHOSEN
            self.sheets_widget.add_widget(sheet_button)
        self.add_widget(self.coin_name_input)
        self.add_widget(self.scroll_sheets)
        self.add_widget(self.cell_input)

        self.add_widget(self.checkboxes_currency)
        self.add_widget(self.checkbox_currency_labels)

        buttons = BoxLayout(orientation="horizontal", size_hint=(1, 0.4))
        self.add_widget(buttons)
        self.button_modify = ButtonC(
            text=language.get_text(Text.MODIFY.value),
            on_release=self.modify,
            size_hint=(0.5, 0.8),
        )
        buttons.add_widget(self.button_modify)
        self.button_delete = ButtonC(
            text=language.get_text(Text.DELETE.value),
            on_release=self.delete,
            size_hint=(0.5, 0.8),
        )
        self.button_delete.color = ERROR_COLOR
        buttons.add_widget(self.button_delete)

    def get_chosen_currency(self):
        return Currency(self.coin.chosen_currency)

    def on_checkbox_active(self, instance, value):
        if instance == self.checkbox_usd:
            if value:
                self.checkbox_eur.active = False
                self.checkbox_gbp.active = False
                self.checkbox_pln.active = False
        if instance == self.checkbox_eur:
            if value:
                self.checkbox_usd.active = False
                self.checkbox_gbp.active = False
                self.checkbox_pln.active = False
        if instance == self.checkbox_gbp:
            if value:
                self.checkbox_usd.active = False
                self.checkbox_eur.active = False
                self.checkbox_pln.active = False
        if instance == self.checkbox_pln:
            if value:
                self.checkbox_usd.active = False
                self.checkbox_gbp.active = False
                self.checkbox_eur.active = False
        if (
            self.checkbox_usd.active
            or self.checkbox_gbp.active
            or self.checkbox_eur.active
            or self.checkbox_pln.active
        ):
            self.label_usd.color = NAME_OK
            self.label_eur.color = NAME_OK
            self.label_gbp.color = NAME_OK
            self.label_pln.color = NAME_OK
        else:
            self.label_usd.color = ERROR_COLOR
            self.label_eur.color = ERROR_COLOR
            self.label_gbp.color = ERROR_COLOR
            self.label_pln.color = ERROR_COLOR

    def chosen_sheet(self, dt: Button):
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

    def modify(self, dt: ButtonC):
        dt.press_color()

        data = self.workbook["data"]
        price = self.check_input_data()
        if price[0]:
            chosen_currency: Currency
            if self.checkbox_usd.active:
                chosen_currency = Currency.USD
            elif self.checkbox_eur.active:
                chosen_currency = Currency.EUR
            elif self.checkbox_gbp.active:
                chosen_currency = Currency.GBP
            else:
                chosen_currency = Currency.PLN
            self.coin.chosen_currency = chosen_currency

            data = self.workbook["data"]
            data.cell(row=1, column=self.coin.id).value = (
                self.coin_name_input.text.lower()
                if self.coin_name_input.text != ""
                else self.coin.name.lower()
            )
            data.cell(row=2, column=self.coin.id).value = self.worksheet_input
            data.cell(row=3, column=self.coin.id).value = self.cell_input.text.upper()
            data.cell(row=4, column=self.coin.id).value = chosen_currency.name
            self.workbook.save(language.read_file()["path_to_xlsx"])
            for coin in self.scrollapp.coins_tab:
                if coin.id == self.coin.id:
                    coin.name = (
                        self.coin_name_input.text.lower()
                        if self.coin_name_input.text != ""
                        else self.coin.name
                    )
                    coin.worksheet = self.worksheet_input
                    coin.cell = self.cell_input.text.upper()
                    coin.price_usd = price[1][Currency.USD]
                    coin.price_pln = price[1][Currency.PLN]
                    coin.price_gbp = price[1][Currency.GBP]
                    coin.price_eur = price[1][Currency.EUR]
                    break
            self.scrollapp.initialize_coins()
            self.popup.dismiss()
        else:
            dt.unpress_color()

    def delete(self, dt: ButtonC):
        dt.press_color()

        data = self.workbook["data"]
        data.cell(row=1, column=self.coin.id).value = "-"
        data.cell(row=2, column=self.coin.id).value = ""
        data.cell(row=3, column=self.coin.id).value = ""
        self.workbook.save(language.read_file()["path_to_xlsx"])
        for coin in self.scrollapp.coins_tab:
            if coin.id == self.coin.id:
                self.scrollapp.coins_tab.remove(coin)
                break
        self.scrollapp.initialize_coins()
        self.scrollapp.coins.height = (
            self.scrollapp.SPACING
            + self.scrollapp.COIN_HEIGHT * len(self.scrollapp.coins_tab)
        )
        self.popup.dismiss()

    def check_input_data(self) -> List[Union[bool, Dict[Currency, str]]]:
        if not self.coin_name_input.text in (self.coin.name, ""):
            test_price: Dict[Currency, str] = Update().get_asset_price(
                self.coin_name_input.text
            )
        else:
            test_price = {
                Currency.USD: self.coin.price_usd,
                Currency.PLN: self.coin.price_pln,
                Currency.GBP: self.coin.price_gbp,
                Currency.EUR: self.coin.price_eur,
            }

        name_ok: bool = False
        sheet_ok: bool = False
        cell_ok: bool = False
        currency_ok: bool = False
        ##############################################
        if test_price not in (
            None,
            {
                Currency.USD: "0,0",
                Currency.PLN: "0,0",
                Currency.GBP: "0,0",
                Currency.EUR: "0,0",
            },
        ):
            self.coin_name_input.text_ok()
            name_ok = True
        else:
            self.coin_name_input.text_error()
        ##############################################
        if "data" not in self.workbook.sheetnames:
            self.workbook.create_sheet("data")
            hidden = self.workbook["data"]
            hidden.sheet_state = "hidden"
            self.workbook.save(language.read_file()["path_to_xlsx"])
        if self.worksheet_input != "":
            sheet_ok = True
        else:
            for sheet in self.sheets_widget.children:
                sheet.color = ERROR_COLOR
        ##############################################
        cell_pattern = r"^[A-Za-z]\d+$"
        if re.match(cell_pattern, self.cell_input.text):
            self.cell_input.text_ok()
            cell_ok = True
        else:
            self.cell_input.text_error()
        ##############################################
        if (
            self.checkbox_usd.active
            or self.checkbox_eur.active
            or self.checkbox_gbp.active
            or self.checkbox_pln.active
        ):
            currency_ok = True
        ##############################################
        return [name_ok & sheet_ok & cell_ok & currency_ok, test_price]
