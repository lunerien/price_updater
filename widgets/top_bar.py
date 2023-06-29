from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from widgets.scroll_app import ScrollApp
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR
from widgets.add_menu import AddMenu

class TopBar(BoxLayout):
    def __init__(self, scrollapp:ScrollApp, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        change_loc_button = Button(text='Change xlsx sheet', size_hint=(0.45, 1), background_color=UNPRESSED_COLOR)
        add_new_coin_button = Button(text='Add new coin', size_hint=(0.45, 1), background_color=UNPRESSED_COLOR)
        change_lang_button = Button(text='EN', size_hint=(0.1, 1), background_color=UNPRESSED_COLOR)
        change_loc_button.bind(on_release=self.change_loc)
        add_new_coin_button.bind(on_release=self.add_new_coin)
        change_lang_button.bind(on_release=self.change_lang)
        self.add_widget(change_loc_button)
        self.add_widget(add_new_coin_button)
        self.add_widget(change_lang_button)

    def change_loc(self, dt):
        print('change xlsx sheet')

    def add_new_coin(self, dt):
        add_coin_menu = Popup(size_hint=(None, None), size=(250, 250), auto_dismiss=True, title='Add new coin', background_color = UNPRESSED_COLOR)
        add_menu = AddMenu(self.scrollapp, add_coin_menu)
        add_coin_menu.content = add_menu
        add_coin_menu.open(animation=True)

    def change_lang(self, dt):
        print('change language')



        
