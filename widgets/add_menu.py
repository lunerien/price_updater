from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from widgets.scroll_app import ScrollApp
from widgets.coin_button import CoinButton


class AddMenu(BoxLayout):
    def __init__(self, scrollApp:ScrollApp, popup:Popup, **kwargs):
        super(AddMenu, self).__init__(**kwargs)
        self.scrollapp = scrollApp
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.coin_name_input = TextInput(text="Coin name")
        self.add_widget(Label(text="Add new coin"))
        self.add_widget(self.coin_name_input)
        self.add_widget(Button(text="Add!", on_release=self.add_this_coin))

    def add_this_coin(self, dt):
        new_button = CoinButton(scrollapp=self.scrollapp, name=self.coin_name_input.text)
        self.scrollapp.coins.add_widget(new_button)
        self.scrollapp.coins_counter += 1
        self.scrollapp.coins.height = ScrollApp.SPACING + CoinButton.COIN_HEIGHT * self.scrollapp.coins_counter
        self.popup.dismiss()