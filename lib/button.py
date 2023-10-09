from typing import Any
from kivymd.uix.button import MDRaisedButton
from kivymd.font_definitions import theme_font_styles

from lib.config import COLOR_BUTTON, COLOR_ORANGE_THEME


class ButtonC(MDRaisedButton):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.font_style = theme_font_styles[5]
        self.font_size: int = 17
        self.md_bg_color: list[float] = COLOR_BUTTON
        self.text_color: list[float] = COLOR_ORANGE_THEME
