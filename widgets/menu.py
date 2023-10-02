from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from lib.language import language, Text
from widgets.add_menu import AddMenu
from lib.button import ButtonC
from lib.config import VERSION
from lib.config import *


class Menu(RelativeLayout):
    def __init__(self, scrollapp, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        self.button_add = ButtonC(text="+")
        self.button_add.font_size = 22
        self.button_add.size_hint = (0.22, 0.13)
        self.button_add.bind(on_press=self.add_new_coin)
        self.button_add.pos_hint = {"center_x": 1.65, "center_y": 0.12}
        self.info = Label(text=VERSION, font_name="standard", font_size=13, color=WHITE)
        self.info.pos_hint = {"center_x": 0.25, "center_y": 0.023}
        self.add_widget(self.button_add)
        self.add_widget(self.info)

    def add_new_coin(self, dt):
        add_coin_menu = Popup(
            title_color=WHITE,
            overlay_color=BEHIND_WINDOW,
            separator_color=WHITE,
            size_hint=(None, None),
            size=(400, 400),
            auto_dismiss=True,
            title=language.get_text(Text.ADD_NEW_COIN.value),
            background_color=WINDOW,
            title_font=font_config,
        )
        add_menu = AddMenu(self.scrollapp, add_coin_menu)
        add_coin_menu.content = add_menu
        add_coin_menu.open(animation=True)
