from kivymd.uix.button import MDRaisedButton

from lib.config import *


class ButtonC(MDRaisedButton):
    def __init__(self, **kwargs):
        super(ButtonC, self).__init__(**kwargs)
        self.md_bg_color = ASSET_BUTTON
        self.font_name = font_config
        self.font_size = 17
        self.color = WHITE

