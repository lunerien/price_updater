from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label

from lib.language import language, Text
from lib.update import Update
from lib.button import ButtonC
from lib.config import VERSION


class Menu(RelativeLayout):
    def __init__(self, scrollapp, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        self.button = ButtonC(text=language.get_text(Text.UPDATE.value))
        self.button.size_hint = (0.6, 0.2)
        self.button.bind(on_release=self.update)
        self.button.pos_hint = {"center_x": 0.5, "center_y": 0.2}
        self.info = Label(text=VERSION, font_name="standard", font_size=13)
        self.info.pos_hint = {"center_x": 0.68, "center_y": 0.023}
        self.add_widget(self.button)
        self.add_widget(self.info)

    def update(self, dt: ButtonC):
        dt.press_color()
        Update().update(self.scrollapp.coins_tab)
        dt.unpress_color()
