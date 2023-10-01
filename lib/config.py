from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

VERSION = "Price Updater© 1.3b Stable"

LabelBase.register(name="standard", fn_regular=".\Gabarito-SemiBold.ttf")
font_config = "standard"

ERROR_COLOR = get_color_from_hex("##c91010F6")
NAME_OK = get_color_from_hex("#14964a")
SHEET_CHOSEN = get_color_from_hex("#00ff4cF4")
WHITE = get_color_from_hex("#FFFDF5F6")
TEXT_BACKGROUND = get_color_from_hex("#5AC4FF0F")
UNPRESSED_COLOR = get_color_from_hex("#5AC4FF0F")
PRESSED_COLOR = get_color_from_hex("#5AC4FFFF")
TOP_BAR_COLOR = get_color_from_hex("#FFFDF5A0")
WINDOW = get_color_from_hex("#FFFDF5F6")
BEHIND_WINDOW = get_color_from_hex("#00000080")
ASSET_BUTTON = get_color_from_hex("#FFFDF5A0")
