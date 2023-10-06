from typing import Any
from kivymd.uix.button import MDRaisedButton

from lib.config import *


class ButtonC(MDRaisedButton):
    def __init__(self, **kwargs: Any) -> None:
        super(ButtonC, self).__init__(**kwargs)
        self.font_name: str = font_config
        self.font_size: int = 17
        self.md_bg_color: list[float] = COLOR_BUTTON
        self.text_color: list[float] = COLOR_ORANGE_THEME
