from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

VERSION = "Price Updater© 1.4b"

LabelBase.register(name="standard", fn_regular=".\Gabarito-SemiBold.ttf")
font_config = "standard"

ERROR_COLOR = get_color_from_hex("#FF3333")
NAME_OK = get_color_from_hex("#90EE90")
SHEET_CHOSEN = get_color_from_hex("#90EE90")
WHITE = get_color_from_hex("#222222")
TEXT_BACKGROUND = get_color_from_hex("#5AC4FF0F")
TOP_BAR = get_color_from_hex("#808080DD")
UNPRESSED_COLOR = get_color_from_hex("#FFFDF5AA")
ORANGE_2 = get_color_from_hex("#E06600")
WINDOW = get_color_from_hex("#FFFDF5F6")
BEHIND_WINDOW = get_color_from_hex("#000000CC")
SHEETS = get_color_from_hex("#FFFFFF55")
FLOATING_BUTTON = get_color_from_hex("#0000000")
CHECKBOX = [80, 80, 80, 1]
ASSET_BUTTON = get_color_from_hex("#CC6600BB")

