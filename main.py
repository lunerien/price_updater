from kivy.core.window import Window
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
import sys
import ctypes

TITLE = "Price Updater"

if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


class CoinButton(Button):
    COIN_HEIGHT = 40

    def __init__(self, scrollapp, name: str = 'bitcoin'):
        super().__init__()
        self.scrollapp = scrollapp
        self.text: str = name
        self.height = self.COIN_HEIGHT
        self.background_color=(1,1,1,0.8)

    def on_release(self):
        #TO_DO
        pass
        

class ScrollApp(ScrollView):
    AMOUNT_OF_COINS = 1
    SPACING = 2

    def __init__(self):
        super().__init__()
        self.coins = GridLayout(cols=1, spacing=self.SPACING, size_hint_y=None)
        self.add_widget(self.coins)
        self.coins_counter = 0
        self.initialize_coins()
        self.coins.height = self.SPACING + CoinButton.COIN_HEIGHT * self.AMOUNT_OF_COINS

    def initialize_coins(self):
        for _ in range(self.AMOUNT_OF_COINS):
            coin_button = CoinButton(scrollapp=self)
            self.coins.add_widget(coin_button)
            self.coins_counter += 1


class Menu(RelativeLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        button = Button(text='Update')
        button.size_hint = (0.6, 0.1)
        button.bind(on_release=self.update)
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
        self.add_widget(button)
    
    def update(self, dt):
        #TO_DO
        pass


class TopBar(BoxLayout):
    def __init__(self, scrollapp:ScrollApp, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.scrollapp = scrollapp
        change_loc_button = Button(text='Change xlsx sheet', size_hint=(0.45, 1))
        add_new_coin_button = Button(text='Add new coin', size_hint=(0.45, 1))
        change_lang_button = Button(text='EN', size_hint=(0.1, 1))
        add_new_coin_button.bind(on_release=self.add_coin)
        self.add_widget(change_loc_button)
        self.add_widget(add_new_coin_button)
        self.add_widget(change_lang_button)

    def add_coin(self, dt):
        new_button = CoinButton(scrollapp=self.scrollapp)
        self.scrollapp.coins.add_widget(new_button)
        self.scrollapp.coins_counter += 1
        self.scrollapp.coins.height = ScrollApp.SPACING + CoinButton.COIN_HEIGHT * self.scrollapp.coins_counter


class MainApp(App):
    def on_start(self, *args):
        HEIGHT = 385
        WIDTH = 850
        Window.set_title(TITLE)
        Window.size = (WIDTH, HEIGHT)
 
    def build(self):
        self.window = BoxLayout(orientation="vertical")
        background = Image(source='images/background.jpg')
        self.scrollview = ScrollApp()
        self.top_bar = TopBar(size_hint=(1, 0.08), scrollapp=self.scrollview)
        self.menu = RelativeLayout(size_hint=(1, 0.91))
        self.window.add_widget(self.top_bar)
        self.menu.add_widget(background)
        self.window.add_widget(self.menu)
        self.scroll_and_menu = BoxLayout(orientation='horizontal')
        self.left_side = BoxLayout(size_hint=(0.8, 1))
        self.right_side = Menu(size_hint=(0.3, 1))
        self.scroll_and_menu.add_widget(self.left_side)
        self.scroll_and_menu.add_widget(self.right_side)
        self.menu.add_widget(self.scroll_and_menu)
        self.left_side.add_widget(self.scrollview)
        return self.window


if __name__ == '__main__':
    MainApp().run()
