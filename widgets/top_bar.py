from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from widgets.scroll_app import ScrollApp
from widgets.coin_button import CoinButton


class TopBar(BoxLayout):
    def __init__(self, scrollapp:ScrollApp, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        change_loc_button = Button(text='Change xlsx sheet', size_hint=(0.45, 1), background_color=(6,2,0,1))
        add_new_coin_button = Button(text='Add new coin', size_hint=(0.45, 1), background_color=(6,2,0,1))
        change_lang_button = Button(text='EN', size_hint=(0.1, 1), background_color=(6,2,0,1))
        add_new_coin_button.bind(on_release=self.add_coin)
        self.add_widget(change_loc_button)
        self.add_widget(add_new_coin_button)
        self.add_widget(change_lang_button)

    def add_coin(self, dt):
        new_button = CoinButton(scrollapp=self.scrollapp)
        self.scrollapp.coins.add_widget(new_button)
        self.scrollapp.coins_counter += 1
        self.scrollapp.coins.height = ScrollApp.SPACING + CoinButton.COIN_HEIGHT * self.scrollapp.coins_counter
