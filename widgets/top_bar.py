from typing import Any
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

from widgets.menu import Menu
from widgets.scroll_app import ScrollApp
from lib.button import ButtonC
from widgets.change_xlsx_menu import ChangeXlsxMenu
from lib.language import language, Languages, Text
from lib.update import Update
from lib.config import *


class TopBar(BoxLayout):
    def __init__(self, scrollapp: ScrollApp, right_side: Menu, **kwargs: Any) -> None:
        super(TopBar, self).__init__(**kwargs)
        self.height = 35
        self.scrollapp = scrollapp
        self.right_side = right_side
        self.change_loc_button = ButtonC(
            text=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value),
            size_hint=(0.45, 1),
        )
        self.change_loc_button.md_bg_color = color_top_bar
        self.update_button = ButtonC(
            text=language.get_text(Text.UPDATE.value),
            size_hint=(0.45, 1),
        )
        self.update_button.md_bg_color = color_top_bar
        self.language_list_buttons = DropDown()
        self.btn_en = ButtonC(
            text=Languages.EN.value,
            size_hint=(1, None),
            height=40,
        )
        self.btn_en.md_bg_color = color_top_bar
        self.btn_pl = ButtonC(
            text=Languages.PL.value,
            size_hint=(1, None),
            height=40,
        )
        self.btn_pl.md_bg_color = color_top_bar
        self.btn_de = ButtonC(
            text=Languages.DE.value,
            size_hint=(1, None),
            height=40,
        )
        self.btn_de.md_bg_color = color_top_bar
        self.btn_en.bind(on_release=self.change_language)
        self.btn_pl.bind(on_release=self.change_language)
        self.btn_de.bind(on_release=self.change_language)
        self.language_list_buttons.add_widget(self.btn_en)
        self.language_list_buttons.add_widget(self.btn_pl)
        self.language_list_buttons.add_widget(self.btn_de)
        self.language_button = ButtonC(
            text=language.get_current_language(),
            size_hint=(0.1, 1),
            pos=(350, 300),
        )
        self.language_button.md_bg_color = color_top_bar
        self.language_button.bind(on_release=self.language_list_buttons.open)
        self.language_list_buttons.bind(
            on_select=lambda instance, x: setattr(
                self.language_button, "text_language", x
            )
        )

        self.change_loc_button.bind(on_release=self.change_loc)
        self.update_button.bind(on_release=self.update)
        self.add_widget(self.change_loc_button)
        self.add_widget(BoxLayout(size_hint=(0.002, 1)))
        self.add_widget(self.update_button)
        self.add_widget(BoxLayout(size_hint=(0.002, 1)))
        self.add_widget(self.language_button)

    def update(self, dt: ButtonC) -> None:
        Update().update(self.scrollapp.coins_tab)

    def change_loc(self, dt: ButtonC) -> None:
        change_xlsx_menu = Popup(
            title_color=COLOR_ORANGE_THEME,
            overlay_color=COLOR_BEHIND_WINDOW,
            separator_color=COLOR_ORANGE_THEME,
            size_hint=(None, None),
            size=(500, 150),
            auto_dismiss=True,
            title=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value),
            background_color=COLOR_WINDOW,
            title_font=font_config,
        )
        add_menu = ChangeXlsxMenu(self.scrollapp, change_xlsx_menu)
        change_xlsx_menu.content = add_menu
        change_xlsx_menu.open(animation=True)

    def change_language(self, dt: ButtonC) -> None:
        self.language_list_buttons.dismiss()
        self.language_button.text = dt.text
        language.change_language(Languages(dt.text))
        self.scrollapp.empty_list.text = language.get_text(Text.EMPTY_LIST_TEXT.value)
        self.change_loc_button.text = language.get_text(Text.CHANGE_XLSX_WORKBOOK.value)
        self.update_button.text = language.get_text(Text.UPDATE.value)
