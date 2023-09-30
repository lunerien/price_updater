from kivy.uix.textinput import TextInput

from lib.config import *


class TextInputC(TextInput):
    def __init__(self, **kwargs):
        super(TextInputC, self).__init__(**kwargs)
        self.size_hint = (1, 0.2)
        self.multiline = False
        self.background_color = TEXT_BACKGROUND
        self.foreground_color = WHITE
        self.cursor_color = WHITE

    def text_ok(self):
        self.foreground_color = NAME_OK

    def text_error(self):
        self.foreground_color = ERROR_COLOR
