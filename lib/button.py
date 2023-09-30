from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


UNPRESSED_COLOR = get_color_from_hex("#5AC4FB15")
PRESSED_COLOR = get_color_from_hex("#5AC4FBF2")


class ButtonC(Button):
    def __init__(self, **kwargs):
        super(ButtonC, self).__init__(**kwargs)
        self.background_color = UNPRESSED_COLOR

    def press_color(self):
        self.background_color = PRESSED_COLOR

    def unpress_color(self):
        self.background_color = UNPRESSED_COLOR
