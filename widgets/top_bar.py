from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

from widgets.scroll_app import ScrollApp
from widgets.menu import TOP_BAR_COLOR, PRESSED_COLOR, UNPRESSED_COLOR
from widgets.add_menu import AddMenu
from widgets.change_xlsx_menu import ChangeXlsxMenu
from lib.language import language, Languages, Text


class TopBar(BoxLayout):
    def __init__(self, scrollapp:ScrollApp, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        change_loc_button = Button(text=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value), size_hint=(0.45, 1), background_color=TOP_BAR_COLOR)
        add_new_coin_button = Button(text=language.get_text(Text.ADD_NEW_COIN.value), size_hint=(0.45, 1), background_color=TOP_BAR_COLOR)

        self.dropdown2 = DropDown()
        dollar_button = Button(text="USD", size_hint_y = None, height = 40, background_color=TOP_BAR_COLOR)
        euro_button = Button(text="EUR", size_hint_y = None, height = 40, background_color=TOP_BAR_COLOR)
        pln_button = Button(text="PLN", size_hint_y = None, height = 40, background_color=TOP_BAR_COLOR)
        dollar_button.bind(on_release = self.change_currency)
        euro_button.bind(on_release = self.change_currency)
        pln_button.bind(on_release = self.change_currency)
        self.dropdown2.add_widget(dollar_button)
        self.dropdown2.add_widget(euro_button)
        self.dropdown2.add_widget(pln_button)
        self.mainbutton2 = Button(text="USD", size_hint =(0.1, 1), pos =(350, 300), background_color=TOP_BAR_COLOR)
        self.mainbutton2.bind(on_release = self.dropdown2.open)
        self.dropdown2.bind(on_select = lambda instance, x: setattr(self.mainbutton2, 'text_currency', x))
        
        self.dropdown = DropDown()
        self.btn_en = Button(text=Languages.EN.value, size_hint_y = None, height = 40, background_color=TOP_BAR_COLOR)
        self.btn_pl = Button(text=Languages.PL.value, size_hint_y = None, height = 40, background_color=TOP_BAR_COLOR)
        self.btn_en.bind(on_release =self.change_language)
        self.btn_pl.bind(on_release =self.change_language)
        self.dropdown.add_widget(self.btn_en)
        self.dropdown.add_widget(self.btn_pl)
        self.mainbutton = Button(text=language.get_current_language(), size_hint =(0.1, 1), pos =(350, 300), background_color=TOP_BAR_COLOR)
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text_language', x))
        
        change_loc_button.bind(on_release=self.change_loc)
        add_new_coin_button.bind(on_release=self.add_new_coin)
        self.add_widget(change_loc_button)
        self.add_widget(add_new_coin_button)
        self.add_widget(self.mainbutton2)
        self.add_widget(self.mainbutton)
        
    def change_loc(self, dt):
        change_xlsx_menu = Popup(size_hint=(None, None), size=(500, 150), auto_dismiss=True, title=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value), background_color = TOP_BAR_COLOR)
        add_menu = ChangeXlsxMenu(self.scrollapp, change_xlsx_menu)
        change_xlsx_menu.content = add_menu
        change_xlsx_menu.open(animation=True)

    def add_new_coin(self, dt):
        add_coin_menu = Popup(size_hint=(None, None), size=(400, 300), auto_dismiss=True, title=language.get_text(Text.ADD_NEW_COIN.value), background_color = TOP_BAR_COLOR)
        add_menu = AddMenu(self.scrollapp, add_coin_menu)
        add_coin_menu.content = add_menu
        add_coin_menu.open(animation=True)

    def change_language(self, dt):
        self.dropdown.dismiss()
        self.mainbutton.text = dt.text
        language.change_language(Languages(dt.text))

    def change_currency(self, dt):
        self.dropdown2.dismiss()
        self.mainbutton2.text = dt.text
        print(f"ustawiam walute: {dt.text}")
