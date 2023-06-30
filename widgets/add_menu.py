from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from widgets.scroll_app import ScrollApp
from widgets.coin_button import CoinButton
from lib.coin import Coin
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR

class AddMenu(BoxLayout):
    def __init__(self, scrollApp:ScrollApp, popup:Popup, **kwargs):
        super(AddMenu, self).__init__(**kwargs)
        self.scrollapp = scrollApp
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.coin_name_input = TextInput(text="Coin name", size_hint=(1, 0.5), multiline=False)
        self.worksheet_name_input = TextInput(text="Worksheet name", size_hint=(1, 0.5), multiline=False)
        self.cell_input = TextInput(text="Cell", size_hint=(1, 0.5), multiline=False)
        self.add_widget(self.coin_name_input)
        self.add_widget(self.worksheet_name_input)
        self.add_widget(self.cell_input)
        buttons = BoxLayout(orientation='horizontal')
        self.add_widget(buttons)
        buttons.add_widget(Button(text="Add!", on_release=self.add_this_coin, size_hint=(0.4, 0.7),
                               background_color=UNPRESSED_COLOR))
        

    def add_this_coin(self, dt):
        dt.background_color=PRESSED_COLOR
        new_coin = Coin(name=self.coin_name_input.text, worksheet=self.worksheet_name_input.text, cell=self.cell_input.text)
        self.scrollapp.coins_tab.append(new_coin)
        self.scrollapp.coins.height = ScrollApp.SPACING + ScrollApp.COIN_HEIGHT * len(self.scrollapp.coins_tab)
        self.scrollapp.initialize_coins()
        self.popup.dismiss()
