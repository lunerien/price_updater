from typing import Tuple
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

from lib.language import language, Text

ERROR_COLOR = get_color_from_hex("##c91010F6")
NAME_OK = get_color_from_hex("#14964a")
SHEET_CHOSEN = get_color_from_hex("#00ff4cF4")
WHITE = get_color_from_hex("#F9F6EEF6")
TEXT_BACKGROUND = get_color_from_hex("#0a2036")


class AutoSuggestionText(TextInput):
    def __init__(self, suggestions: Tuple[str, ...], **kwargs):
        super(AutoSuggestionText, self).__init__(**kwargs)
        self.suggestion_coins = suggestions
        self.text_chosen = None
        self.dropdown = None
        self.multiline = False
        self.size_hint = (1, 0.2)
        self.background_color = TEXT_BACKGROUND
        self.foreground_color = WHITE
        self.focus = True
        self.cursor_color = WHITE
        self.select_all()

    def text_ok(self):
        self.foreground_color = NAME_OK

    def text_error(self):
        self.foreground_color = ERROR_COLOR

    @staticmethod
    def on_text(self, value):
        if value != language.get_text(Text.COIN_NAME.value):
            if self.dropdown:
                self.dropdown.dismiss()

            self.dropdown = DropDown()

            def push(dt):
                self.dropdown.dismiss()
                self.text_chosen = dt.text
                self.push_text(dt)

            if self.text_chosen != value and self.text != "":
                for suggestion in self.suggestion_coins:
                    if suggestion.startswith(value.lower()):
                        button = Button(
                            text=suggestion,
                            size_hint_y=None,
                            height=32,
                            on_release=push,
                            background_color=TEXT_BACKGROUND,
                        )
                        self.dropdown.add_widget(button)
                if self.dropdown.children:
                    Clock.schedule_once(lambda dt: self.dropdown.open(self))

    def push_text(self, dt):
        self.text = dt.text
        self.dropdown = None
