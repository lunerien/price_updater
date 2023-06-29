from kivy.uix.button import Button
from kivy.uix.popup import Popup

from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR
from widgets.modify_coin import ModifyCoin


class CoinButton(Button):
    COIN_HEIGHT = 40

    def __init__(self, scrollapp, name: str = 'bitcoin'):
        super().__init__()
        self.scrollapp = scrollapp
        self.text: str = name
        self.height = self.COIN_HEIGHT
        self.background_color=UNPRESSED_COLOR

    def on_release(self):
        self.background_color=UNPRESSED_COLOR
        modify_coin_menu = Popup(size_hint=(None, None), size=(250, 250), auto_dismiss=True, title='Modify coin', background_color = UNPRESSED_COLOR)
        add_menu = ModifyCoin(modify_coin_menu, self.text)
        modify_coin_menu.content = add_menu
        modify_coin_menu.open(animation=True)


    def on_press(self):
        self.background_color=PRESSED_COLOR




    
