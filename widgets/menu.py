from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class Menu(RelativeLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        button = Button(text='Update', background_color=(4,2,0,1))
        button.size_hint = (0.6, 0.1)
        button.bind(on_release=self.update, on_press=self.on_button_press)
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.2}
        self.add_widget(button)
    
    def update(self, dt):
        print("update")
        dt.background_color=(4,2,0,1)

    def on_button_press(self, dt):
        dt.background_color = (4,1,0,0.8)
