from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivy.uix.gridlayout import GridLayout

from widgets.scroll_app import ScrollApp
from lib.update import Update
from lib.language import language, Text
from widgets.menu import UNPRESSED_COLOR, PRESSED_COLOR

ERROR_COLOR = get_color_from_hex("##c91010F6")
SHEET_CHOSEN = get_color_from_hex("#00ff4cF4")

class AddMenu(BoxLayout):
    def __init__(self, scrollApp:ScrollApp, popup:Popup, **kwargs):
        super(AddMenu, self).__init__(**kwargs)
        self.scrollapp = scrollApp
        self.popup = popup
        self.orientation = "vertical"
        self.opacity = 0.8
        self.workbook = Update().try_load_workbook()
        self.spacing = 10

        if self.workbook != None:
            self.build()
        else:
            print("brak arkusza do zapisania!")

    def build(self):
        self.sheets = self.workbook.sheetnames
        self.sheets.remove('data')

        self.scroll_sheets = ScrollView()
        self.sheets_widget = GridLayout(cols=1, spacing=5, size_hint=(1, None), height= 20)
        self.scroll_sheets.add_widget(self.sheets_widget)
        for sheet in self.sheets:
            sheet_button = Button(text=sheet, background_color=UNPRESSED_COLOR, size_hint_y = None, height = 40, on_release=self.chosen_sheet)
            self.sheets_widget.add_widget(sheet_button)
        
        self.coin_name_input = TextInput(text=language.get_text(Text.COIN_NAME.value), size_hint=(1, 0.3), multiline=False)
        self.cell_input = TextInput(text=language.get_text(Text.CELL.value), size_hint=(1, 0.3), multiline=False)
        self.add_widget(self.coin_name_input)
        self.add_widget(self.scroll_sheets)
        self.add_widget(self.cell_input)
        buttons = BoxLayout(orientation='horizontal', size_hint=(1, 0.4))
        self.add_widget(buttons)
        buttons.add_widget(Button(text=language.get_text(Text.ADD.value), on_release=self.add_this_coin, size_hint=(1, 1),
                               background_color=UNPRESSED_COLOR))
    

    def chosen_sheet(self, dt):
        dt.background_color = SHEET_CHOSEN
        print("chosen_sheet")

        
    def add_this_coin(self, dt):
        dt.background_color=PRESSED_COLOR
        
        test_price = Update().get_token_price(self.coin_name_input.text)
        if test_price != None:
            if 'data' in self.workbook.sheetnames:
                None
            else:
                self.workbook.create_sheet('data')
                hidden = self.workbook['data']
                hidden.sheet_state = 'hidden'
                self.workbook.save(language.read_file()['path_to_xlsx'])
            
            data = self.workbook['data']
            i = 1
            while data.cell(row=1, column=i).value != "-" and data.cell(row=1, column=i).value != None:
                i += 1
            
            data.cell(row=1, column=i).value = self.coin_name_input.text
            data.cell(row=2, column=i).value = self.worksheet_name_input.text
            data.cell(row=3, column=i).value = self.cell_input.text
            self.workbook.save(language.read_file()['path_to_xlsx'])
            self.scrollapp.initialize_coins()
            self.scrollapp.coins.height = ScrollApp.SPACING + ScrollApp.COIN_HEIGHT * len(self.scrollapp.coins_tab)
            self.popup.dismiss()
        else:
            self.coin_name_input.foreground_color = ERROR_COLOR
        
