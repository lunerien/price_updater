from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from KivyOnTop import register_topmost
import sys
import ctypes

from widgets.scroll_app import ScrollApp
from widgets.top_bar import TopBar
from widgets.menu import Menu
from lib.language import language, Text


TITLE = "Price Updater"


if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


class MainApp(App):
    def __init__(self, *args):
        super(MainApp, self).__init__(*args)
        self.window = BoxLayout(orientation="vertical")
        self.scrollview = ScrollApp()
        self.background = Image(source='images/background.jpg', allow_stretch=True, keep_ratio=False)
        self.top_bar = TopBar(size_hint=(1, 0.08), scrollapp=self.scrollview)
        self.menu = RelativeLayout(size_hint=(1, 0.91))
        self.scroll_and_menu = BoxLayout(orientation='horizontal')
        self.left_side = BoxLayout(size_hint=(0.8, 1))
        self.right_side = Menu(self.scrollview.coins_tab, size_hint=(0.3, 1))

    def on_start(self, *args):
        HEIGHT = 450
        WIDTH = 900
        Window.minimum_width, Window.minimum_height = WIDTH, HEIGHT
        Window.set_title(TITLE)
        Window.size = (WIDTH, HEIGHT)
        # register_topmost(Window, TITLE)
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        Window.size = (WIDTH, HEIGHT)
        Window.top = screen_height-HEIGHT*1.8
        Window.left = screen_width-WIDTH*1.8
        Window.borderless = True

    def build(self):
        self.window.add_widget(self.top_bar)
        self.menu.add_widget(self.background)
        self.window.add_widget(self.menu)
        self.scroll_and_menu.add_widget(self.left_side)
        self.scroll_and_menu.add_widget(self.right_side)
        self.menu.add_widget(self.scroll_and_menu)
        self.left_side.add_widget(self.scrollview)
        return self.window
    
    def restart(self):
        App.get_running_app().stop()
        MainApp().run()

main_app = MainApp()
if __name__ == '__main__':
    main_app.run()
