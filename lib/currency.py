from enum import Enum
import json
from bs4 import BeautifulSoup
from requests import get
from requests import exceptions


class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    PLN = "PLN"


class CCurrency:
    def __init__(self):
        self.connection_lost: bool = False
        self.data_file = self.read_file()
        self.usd_pln: float = 0.0
        self.eur_pln: float = 0.0
        self.gbp_pln: float = 0.0

    def get_currency(self, currency: Currency) -> float:
        try:
            url = f"https://www.biznesradar.pl/notowania/{currency.value}PLN#1d_lin_lin"
            page = get(url)
            bs = BeautifulSoup(page.content, "html.parser")

            for nastronie in bs.find_all("span", class_="profile_quotation"):
                price = nastronie.find("span", class_="q_ch_act")
                price = str(price)
                price = price.replace('<span class="q_ch_act">', "")
                price = price.replace("</span>", "")
                price = price[0:6]
                return float(price)
        except (
            ValueError,
            ZeroDivisionError,
            TypeError,
            exceptions.ConnectionError,
        ) as e:
            if isinstance(e, exceptions.ConnectionError):
                self.connection_lost = True
            return 0.0
        return 0.0

    def return_price(self, currency: Currency) -> float:
        match currency:
            case Currency.PLN:
                return 1.0
            case Currency.USD:
                return self.usd_pln
            case Currency.GBP:
                return self.gbp_pln
            case Currency.EUR:
                return self.eur_pln
        return 0.0

    def get_current_currency(self) -> Currency:
        self.data_file = self.read_file()
        return Currency(self.data_file["chosen_currency"])

    def read_file(self) -> str:
        file = open("data.json")
        data = json.load(file)
        return data

    def change_currency(self, new_currency: Currency):
        with open("data.json", "r+") as file:
            data = json.load(file)
            data["chosen_currency"] = new_currency.value
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        self.language_file = self.read_file()


currency = CCurrency()
