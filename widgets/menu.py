from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import get_color_from_hex

from lib.language import language, Text
from lib.update import Update


UNPRESSED_COLOR = get_color_from_hex("#5AC4FB38")
PRESSED_COLOR = get_color_from_hex("#5AC4FBF2")
TOP_BAR_COLOR = get_color_from_hex("#5AC4FBFF")
UPDATING = get_color_from_hex("#00C44cF4")


class Menu(RelativeLayout):
    def __init__(self, coins,**kwargs):
        super(Menu, self).__init__(**kwargs)
        button = Button(text=language.get_text(Text.UPDATE.value), background_color=UNPRESSED_COLOR)
        button.size_hint = (0.6, 0.1)
        button.bind(on_release=self.update, on_press=self.on_button_press)
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
        self.add_widget(button)
        self.coins = coins
    
    def update(self, dt):
        dt.background_color=PRESSED_COLOR
        Update().update(self.coins)

    def on_button_press(self, dt):
        dt.background_color=PRESSED_COLOR
