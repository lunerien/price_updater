from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import get_color_from_hex

from lib.language import language, Text
from lib.update import Update
from lib.button import ButtonC

TOP_BAR_COLOR = get_color_from_hex("#5AC4FB35")
UPDATING = get_color_from_hex("#5AC4FBF2")
ERROR_COLOR = get_color_from_hex("##c91010F6")
UNPRESSED_COLOR = get_color_from_hex("#5AC4FB15")
PRESSED_COLOR = get_color_from_hex("#5AC4FBF2")


class Menu(RelativeLayout):
    def __init__(self, scrollapp, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        self.button = ButtonC(text=language.get_text(Text.UPDATE.value))
        self.button.size_hint = (0.6, 0.2)
        self.button.bind(on_release=self.update)
        self.button.pos_hint = {"center_x": 0.5, "center_y": 0.2}
        self.add_widget(self.button)

    def update(self, dt: ButtonC):
        dt.press_color()
        Update().update(self.scrollapp.coins_tab)
        dt.unpress_color()
