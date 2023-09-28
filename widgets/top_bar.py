from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

from widgets.menu import Menu
from widgets.scroll_app import ScrollApp
from widgets.menu import TOP_BAR_COLOR
from widgets.add_menu import AddMenu
from widgets.change_xlsx_menu import ChangeXlsxMenu
from lib.language import language, Languages, Text
from lib.currency import currency, Currency


class TopBar(BoxLayout):
    def __init__(self, scrollapp: ScrollApp, right_side: Menu, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        self.right_side = right_side
        self.change_loc_button = Button(
            text=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value),
            size_hint=(0.45, 1),
            background_color=TOP_BAR_COLOR,
        )
        self.add_new_coin_button = Button(
            text=language.get_text(Text.ADD_NEW_COIN.value),
            size_hint=(0.45, 1),
            background_color=TOP_BAR_COLOR,
        )

        self.currency_list_buttons = DropDown()
        dollar_button = Button(
            text="USD", size_hint_y=None, height=40, background_color=TOP_BAR_COLOR
        )
        pln_button = Button(
            text="PLN", size_hint_y=None, height=40, background_color=TOP_BAR_COLOR
        )
        dollar_button.bind(on_release=self.change_currency)
        pln_button.bind(on_release=self.change_currency)
        self.currency_list_buttons.add_widget(dollar_button)
        self.currency_list_buttons.add_widget(pln_button)
        self.currency_button = Button(
            text=currency.get_current_currency().value,
            size_hint=(0.1, 1),
            pos=(350, 300),
            background_color=TOP_BAR_COLOR,
        )
        self.currency_button.bind(on_release=self.currency_list_buttons.open)
        self.currency_list_buttons.bind(
            on_select=lambda instance, x: setattr(
                self.currency_button, "text_currency", x
            )
        )

        self.language_list_buttons = DropDown()
        self.btn_en = Button(
            text=Languages.EN.value,
            size_hint_y=None,
            height=40,
            background_color=TOP_BAR_COLOR,
        )
        self.btn_pl = Button(
            text=Languages.PL.value,
            size_hint_y=None,
            height=40,
            background_color=TOP_BAR_COLOR,
        )
        self.btn_en.bind(on_release=self.change_language)
        self.btn_pl.bind(on_release=self.change_language)
        self.language_list_buttons.add_widget(self.btn_en)
        self.language_list_buttons.add_widget(self.btn_pl)
        self.language_button = Button(
            text=language.get_current_language(),
            size_hint=(0.1, 1),
            pos=(350, 300),
            background_color=TOP_BAR_COLOR,
        )
        self.language_button.bind(on_release=self.language_list_buttons.open)
        self.language_list_buttons.bind(
            on_select=lambda instance, x: setattr(
                self.language_button, "text_language", x
            )
        )

        self.change_loc_button.bind(on_release=self.change_loc)
        self.add_new_coin_button.bind(on_release=self.add_new_coin)
        self.add_widget(self.change_loc_button)
        self.add_widget(self.add_new_coin_button)
        # self.add_widget(self.currency_button)
        self.add_widget(self.language_button)

    def change_loc(self, dt):
        change_xlsx_menu = Popup(
            size_hint=(None, None),
            size=(500, 150),
            auto_dismiss=True,
            title=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value),
            background_color=TOP_BAR_COLOR,
        )
        add_menu = ChangeXlsxMenu(self.scrollapp, change_xlsx_menu)
        change_xlsx_menu.content = add_menu
        change_xlsx_menu.open(animation=True)

    def add_new_coin(self, dt):
        add_coin_menu = Popup(
            size_hint=(None, None),
            size=(400, 400),
            auto_dismiss=True,
            title=language.get_text(Text.ADD_NEW_COIN.value),
            background_color=TOP_BAR_COLOR,
        )
        add_menu = AddMenu(self.scrollapp, add_coin_menu)
        add_coin_menu.content = add_menu
        add_coin_menu.open(animation=True)

    def change_language(self, dt):
        self.language_list_buttons.dismiss()
        self.language_button.text = dt.text
        language.change_language(Languages(dt.text))
        self.scrollapp.empty_list.text = language.get_text(Text.EMPTY_LIST_TEXT.value)
        self.change_loc_button.text = language.get_text(Text.CHANGE_XLSX_WORKBOOK.value)
        self.add_new_coin_button.text = language.get_text(Text.ADD_NEW_COIN.value)
        self.right_side.button.text = language.get_text(Text.UPDATE.value)

    def change_currency(self, dt):
        self.currency_list_buttons.dismiss()
        self.currency_button.text = dt.text
        currency.change_currency(Currency(dt.text))
        self.scrollapp.initialize_coins()
