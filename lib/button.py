from kivy.uix.button import Button

from lib.config import *



class ButtonC(Button):
    def __init__(self, **kwargs):
        super(ButtonC, self).__init__(**kwargs)
        self.background_color = UNPRESSED_COLOR
        self.font_name = font_config
        self.font_size = 17
        self.color = WHITE

    def press_color(self):
        self.background_color = PRESSED_COLOR

    def unpress_color(self):
        self.background_color = UNPRESSED_COLOR