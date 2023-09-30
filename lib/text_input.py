from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex


ERROR_COLOR = get_color_from_hex("##c91010F6")
NAME_OK = get_color_from_hex("#14964a")
SHEET_CHOSEN = get_color_from_hex("#00ff4cF4")
WHITE = get_color_from_hex("#F9F6EEF6")
TEXT_BACKGROUND = get_color_from_hex("#0a2036")


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
