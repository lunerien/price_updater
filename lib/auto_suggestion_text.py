from typing import Tuple
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.utils import get_color_from_hex

SUGGESTIONS = get_color_from_hex("#0088ff")

class AutoSuggestionText(TextInput):
    def __init__(self, suggestions: Tuple[str], **kwargs):
        super(AutoSuggestionText, self).__init__(**kwargs)
        self.suggestion_coins = suggestions
        self.text_chosen = None
        self.dropdown = None

    @staticmethod
    def on_text(self, value):
        if self.dropdown:
            self.dropdown.dismiss()

        self.dropdown = DropDown()

        def push(dt):
            self.dropdown.dismiss()
            self.text_chosen = dt.text
            self.push_text(dt)

        if self.text_chosen != value and self.text != '':
            for suggestion in self.suggestion_coins:
                if suggestion.startswith(value.lower()):
                    button = Button(text=suggestion, size_hint_y=None, height=32, on_release=push, background_color=SUGGESTIONS)
                    self.dropdown.add_widget(button)
            if self.dropdown.children:
                self.dropdown.open(self)

    def push_text(self, dt):
        self.text = dt.text
        self.dropdown = None
