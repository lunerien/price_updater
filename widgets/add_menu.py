from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from widgets.scroll_app import ScrollApp
from widgets.coin_button import CoinButton
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR

class AddMenu(BoxLayout):
    def __init__(self, scrollApp:ScrollApp, popup:Popup, **kwargs):
        super(AddMenu, self).__init__(**kwargs)
        self.scrollapp = scrollApp
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.coin_name_input = TextInput(text="Coin name", size_hint=(1, 0.2))
        self.workbook_name_input = TextInput(text="workbook name", size_hint=(1, 0.2))
        self.cell_input = TextInput(text="Cell", size_hint=(1, 0.2))
        self.add_widget(self.coin_name_input)
        self.add_widget(self.workbook_name_input)
        self.add_widget(self.cell_input)
        self.add_widget(Button(text="Add!", on_release=self.add_this_coin, size_hint=(0.4, 0.2),
                               pos_hint={'center_x': 0.5, 'center_y': 0.5}, background_color=UNPRESSED_COLOR))

    def add_this_coin(self, dt):
        dt.background_color=PRESSED_COLOR
        new_button = CoinButton(scrollapp=self.scrollapp, name=self.coin_name_input.text)
        self.scrollapp.coins.add_widget(new_button)
        self.scrollapp.coins_counter += 1
        self.scrollapp.coins.height = ScrollApp.SPACING + CoinButton.COIN_HEIGHT * self.scrollapp.coins_counter
        self.popup.dismiss()