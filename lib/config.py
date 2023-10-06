from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

VERSION: str = "Price Updater© 1.4b"

LabelBase.register(name="standard", fn_regular=".\Gabarito-SemiBold.ttf")
font_config: str = "standard"

COLOR_ERROR: list[float] = get_color_from_hex("#FF0000")
COLOR_BUTTON: list[float] = get_color_from_hex("#444444FF")
COLOR_BACKGROUND_INPUT: list[float] = get_color_from_hex("#5AC4FF0F")
COLOR_TOP_BAR: list[float] = get_color_from_hex("#403C3CFF")
COLOR_ORANGE_THEME: list[float] = get_color_from_hex("#E06600")
COLOR_WINDOW: list[float] = get_color_from_hex("#FFFDF5FF")
COLOR_BEHIND_WINDOW: list[float] = get_color_from_hex("#000000CC")
COLOR_CHECKBOX: list[float] = [80, 80, 80, 1]
COLOR_ASSET_BUTTON: list[float] = get_color_from_hex("#FFFDF5BB")
