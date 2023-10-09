from typing import Tuple, Any
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock

from lib.language import language, Text
from lib.config import *


class AutoSuggestionText(TextInput):
    modified_coin: str = ""

    def __init__(self, suggestions: Tuple[str, ...], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.suggestion_coins: Tuple[str, ...] = suggestions
        self.text_chosen: str = ""
        self.dropdown: DropDown = None
        self.multiline: bool = False
        self.size_hint: tuple = (1, 0.2)
        self.background_color: list[float] = COLOR_BACKGROUND_INPUT
        self.foreground_color: list[float] = COLOR_ORANGE_THEME
        self.focus: bool = True
        self.cursor_color: list[float] = COLOR_ORANGE_THEME
        self.font_name: str = "standard"
        self.font_size: int = 16
        self.select_all()
        self.focus = True

    def text_ok(self) -> None:
        self.foreground_color = COLOR_ORANGE_THEME

    def text_error(self) -> None:
        self.foreground_color = COLOR_ERROR

    @staticmethod
    def on_text(cls: TextInput, value: str) -> None:
        if (
            value != language.get_text(Text.COIN_NAME.value)
            and value != AutoSuggestionText.modified_coin
        ):
            if cls.dropdown:
                cls.dropdown.dismiss()
            cls.dropdown = DropDown()

            def push(dt: Button) -> None:
                cls.dropdown.dismiss()
                cls.text_chosen = dt.text
                cls.push_text(dt)

            if cls.text_chosen != value and cls.text != "":
                Clock.unschedule(cls.dropdown.open)
                for suggestion in cls.suggestion_coins:
                    if suggestion.startswith(value.lower()):
                        button = Button(
                            text=suggestion,
                            size_hint_y=None,
                            height=32,
                            on_release=push,
                            background_color=COLOR_BUTTON,
                            font_name=font_config,
                            font_size=14,
                            color=COLOR_ORANGE_THEME,
                        )
                        cls.dropdown.add_widget(button)
                if cls.dropdown.children:
                    cls.dropdown.open(cls)

    def push_text(self, dt: TextInput) -> None:
        self.text = dt.text
        self.dropdown = None
