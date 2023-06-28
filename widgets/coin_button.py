from kivy.uix.button import Button

from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR


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
        print("modify")
        pass

    def on_press(self):
        self.background_color=PRESSED_COLOR

    
