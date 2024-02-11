import sys
import os
import ctypes
from typing import Any
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout

from widgets.scroll_app import ScrollApp
from widgets.top_bar import TopBar
from widgets.menu import Menu


title: str = "Price Updater©"


if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
elif sys.platform.startswith("Linux"):
    os.system("clear")

class MainApp(MDApp):
    def __init__(self, *args: Any) -> None:
        super(MainApp, self).__init__(*args)
        self.window = BoxLayout(orientation="vertical")
        self.menu = RelativeLayout(size_hint=(1, 0.9))
        self.scroll_and_menu = BoxLayout(orientation="horizontal")
        self.top_bar_and_menu = BoxLayout(orientation="vertical")
        self.left_side = FloatLayout(size_hint=(1, 1))
        self.background = Image(source="images/background_sode.jpg", fit_mode="fill")
        self.scrollview = ScrollApp()
        self.right_side = Menu(self.scrollview, size_hint=(0.3, 1))
        self.top_bar = TopBar(
            size_hint=(1, None), scrollapp=self.scrollview, right_side=self.right_side
        )

    def on_start(self, *args: Any) -> None:
        height: int = 500
        width: int = 850
        Window.minimum_width, Window.minimum_height = width, height
        Window.set_title(title)
        Window.size = (width, height)
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        Window.size = (width, height)
        Window.top = screen_height - height * 2
        Window.left = screen_width - width * 2
        Window.borderless = False

    def build(self) -> BoxLayout:
        self.window.add_widget(self.menu)

        self.menu.add_widget(self.background)
        self.menu.add_widget(self.top_bar_and_menu)

        self.top_bar_and_menu.add_widget(self.top_bar)
        self.top_bar_and_menu.add_widget(self.scroll_and_menu)

        self.scroll_and_menu.add_widget(self.left_side)

        self.left_side.add_widget(self.scrollview)
        self.left_side.add_widget(self.right_side)
        return self.window


main_app = MainApp()
if __name__ == "__main__":
    main_app.run()
