from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown

from widgets.scroll_app import ScrollApp
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR
from widgets.add_menu import AddMenu
from lib.language import language, Languages, Text

class TopBar(BoxLayout):
    def __init__(self, scrollapp:ScrollApp, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        change_loc_button = Button(text=language.get_text(Text.CHANGE_XLSX_WORKBOOK.value), size_hint=(0.45, 1), background_color=UNPRESSED_COLOR)
        add_new_coin_button = Button(text=language.get_text(Text.ADD_NEW_COIN.value), size_hint=(0.45, 1), background_color=UNPRESSED_COLOR)
        
        self.dropdown = DropDown()
        self.btn_en = Button(text=Languages.EN.value, size_hint_y = None, height = 25, background_color=PRESSED_COLOR)
        self.btn_pl = Button(text=Languages.PL.value, size_hint_y = None, height = 25, background_color=PRESSED_COLOR)
        self.btn_en.bind(on_release =self.change_language)
        self.btn_pl.bind(on_release =self.change_language)
        self.dropdown.add_widget(self.btn_en)
        self.dropdown.add_widget(self.btn_pl)
        mainbutton = Button(text=language.get_current_language(), size_hint =(0.1, 1), pos =(350, 300), background_color=UNPRESSED_COLOR)
        mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text_language', x))
        
        change_loc_button.bind(on_release=self.change_loc)
        add_new_coin_button.bind(on_release=self.add_new_coin)
        self.add_widget(change_loc_button)
        self.add_widget(add_new_coin_button)
        self.add_widget(mainbutton)

    def change_loc(self, dt):
        pass

    def add_new_coin(self, dt):
        add_coin_menu = Popup(size_hint=(None, None), size=(250, 250), auto_dismiss=True, title=language.get_text(Text.ADD_NEW_COIN.value), background_color = UNPRESSED_COLOR)
        add_menu = AddMenu(self.scrollapp, add_coin_menu)
        add_coin_menu.content = add_menu
        add_coin_menu.open(animation=True)

    def change_language(self, dt):
        self.dropdown.select(dt.text)
        language.change_language(Languages(dt.text))




        
