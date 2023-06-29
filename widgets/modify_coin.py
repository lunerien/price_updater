from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR
DELETE_COLOR = get_color_from_hex("#FF0101e6")


class ModifyCoin(BoxLayout):
    def __init__(self, popup:Popup, name:str, **kwargs):
        super(ModifyCoin, self).__init__(**kwargs)
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.name = name
        self.coin_name_input = TextInput(text=self.name, size_hint=(1, 0.5))
        self.workbook_name_input = TextInput(text="workbook name", size_hint=(1, 0.5))
        self.cell_input = TextInput(text="Cell", size_hint=(1, 0.5))
        self.add_widget(self.coin_name_input)
        self.add_widget(self.workbook_name_input)
        self.add_widget(self.cell_input)
        buttons = BoxLayout(orientation='horizontal')
        self.add_widget(buttons)
        buttons.add_widget(Button(text="Modify!", on_release=self.modify, size_hint=(0.4, 0.7),
                               background_color=UNPRESSED_COLOR))
        buttons.add_widget(Button(text="Delete!", on_release=self.delete, size_hint=(0.4, 0.7),
                               background_color=DELETE_COLOR))
        

    def modify(self, dt):
        dt.background_color=PRESSED_COLOR
        self.popup.dismiss()

    def delete(self, dt):
        dt.background_color=PRESSED_COLOR
        self.popup.dismiss()