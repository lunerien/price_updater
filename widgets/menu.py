from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.uix.button import MDFloatingActionButton

from lib.language import language, Text
from widgets.add_menu import AddMenu
from lib.button import ButtonC
from lib.config import VERSION
from lib.config import *


class Menu(MDRelativeLayout):
    def __init__(self, scrollapp, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        self.button_add = MDFloatingActionButton(
            icon="pencil",
            on_release=self.add_new_coin,
            md_bg_color=WHITE,
            icon_color=ORANGE_2,
            icon_size="25sp",
        )
        self.button_add.pos_hint = {"center_x": 1.67, "center_y": 0.09}
        self.info = Label(
            text=VERSION, font_name="standard", font_size=13, color=ORANGE_2
        )
        self.info.pos_hint = {"center_x": 0.25, "center_y": 0.023}
        self.add_widget(self.button_add)
        self.add_widget(self.info)

    def add_new_coin(self, dt: ButtonC):
        add_coin_menu = Popup(
            title_color=ORANGE_2,
            overlay_color=BEHIND_WINDOW,
            separator_color=ORANGE_2,
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
