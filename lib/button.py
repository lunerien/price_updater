from kivymd.uix.button import MDRaisedButton

from lib.config import *


class ButtonC(MDRaisedButton):
    def __init__(self, **kwargs):
        super(ButtonC, self).__init__(**kwargs)
        self.font_name = font_config
        self.font_size = 17
        self.md_bg_color = COLOR_BUTTON
        self.text_color = COLOR_ORANGE_THEME
