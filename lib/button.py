from kivy.uix.button import Button

from lib.config import *



class ButtonC(Button):
    def __init__(self, **kwargs):
        super(ButtonC, self).__init__(**kwargs)
        self.background_color = ASSET_BUTTON
        self.font_name = font_config
        self.font_size = 17
        self.color = TOP_BAR_COLOR

    def press_color(self):
        self.background_color = BEHIND_WINDOW

    def unpress_color(self):
        self.background_color = TOP_BAR_COLOR
