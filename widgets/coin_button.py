from kivy.uix.button import Button


class CoinButton(Button):
    COIN_HEIGHT = 40

    def __init__(self, scrollapp, name: str = 'bitcoin'):
        super().__init__()
        self.scrollapp = scrollapp
        self.text: str = name
        self.height = self.COIN_HEIGHT
        self.background_color=(4,2,0,0.7)

    def on_release(self):
        self.background_color=(4,2,0,0.6)
        print("modify")
        pass

    def on_press(self):
        self.background_color=(4,1,0,0.9)
