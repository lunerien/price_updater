from kivy.uix.textinput import TextInput

from lib.config import *


class TextInputC(TextInput):
    def __init__(self, **kwargs):
        super(TextInputC, self).__init__(**kwargs)
        self.size_hint = (1, 0.2)
        self.multiline = False
        self.background_color = COLOR_BACKGROUND_INPUT
        self.foreground_color = COLOR_ORANGE_THEME
        self.cursor_color = COLOR_ORANGE_THEME
        self.font_name = "standard"
        self.font_size = 16

    def text_ok(self):
        self.foreground_color = COLOR_ORANGE_THEME

    def text_error(self):
        self.foreground_color = COLOR_ERROR
