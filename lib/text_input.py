from kivy.uix.textinput import TextInput

from lib.config import *


class TextInputC(TextInput):
    def __init__(self, **kwargs):
        super(TextInputC, self).__init__(**kwargs)
        self.size_hint = (1, 0.2)
        self.multiline = False
        self.background_color = TEXT_BACKGROUND
        self.foreground_color = ORANGE_2
        self.cursor_color = ORANGE_2
        self.font_name = "standard"
        self.font_size = 16

    def text_ok(self):
        self.foreground_color = ORANGE_2

    def text_error(self):
        self.foreground_color = ERROR_COLOR
