from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.utils import get_color_from_hex

UNPRESSED_COLOR = get_color_from_hex("#5A56FBE6")
PRESSED_COLOR = get_color_from_hex("#2D64F8E6")


class Menu(RelativeLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        button = Button(text='Update', background_color=UNPRESSED_COLOR)
        button.size_hint = (0.6, 0.1)
        button.bind(on_release=self.update, on_press=self.on_button_press)
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
        self.add_widget(button)
    
    def update(self, dt):
        print("update")
        dt.background_color=UNPRESSED_COLOR

    def on_button_press(self, dt):
        dt.background_color=PRESSED_COLOR
