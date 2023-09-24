from openpyxl import load_workbook
from bs4 import BeautifulSoup
from requests import get
from openpyxl.utils.exceptions import InvalidFileException

from lib.language import language
from lib.currency import currency, Currency

class Update:
    def __init__(self):
        self.workbook = self.try_load_workbook()
        self.chosen_currency = currency.get_current_currency()
    
    def update(self, coins):
        if self.workbook != None:
            data = self.workbook['data']
            i = 1
            while data.cell(row=1, column=i).value != None:
                if data.cell(row=1, column=i).value != "-":
                    match self.chosen_currency:
                        case Currency.USD:
                            price = next(coin.price_usd for coin in coins if coin.name == data.cell(row=1, column=i).value)
                        case Currency.PLN:
                            price = next(coin.price_pln for coin in coins if coin.name == data.cell(row=1, column=i).value)
                    sheet = self.workbook[data.cell(row=2, column=i).value]
                    print(price)
                    sheet[data.cell(row=3, column=i).value] = price
                i += 1
            self.workbook.save(language.read_file()['path_to_xlsx'])

    def get_token_price(self, ticker:str):
        url = f"https://coinmarketcap.com/currencies/{ticker.lower()}"
        page = get(url)
        bs = BeautifulSoup(page.content, "html.parser")
        try:
            for web in bs.find_all(
                "div",
                class_="sc-16891c57-0 hqcKQB flexStart alignBaseline",
            ):
                price_str = str(web.find("span", class_="sc-16891c57-0 dxubiK base-text"))
                price_str = price_str.replace('<span class="sc-16891c57-0 dxubiK base-text">$', "")
                price_str = price_str.replace('</span>', "")
                price_str = price_str.replace(",", "")
                price_float = float(price_str)
                print(price_float)

                price_usd = str(round(price_float, 6)) if price_str[:2] == "0." else str(round(price_float, 2))
                price_usd = price_usd.replace(".", ",")

                price_pln_float = price_float * currency.return_price(Currency.PLN)
                price_pln = str(round(price_pln_float, 6)) if price_str[:2] == "0." else str(round(price_pln_float, 2))
                price_pln = price_pln.replace(".", ",")

                return {Currency.USD: price_usd, Currency.PLN: price_pln}
        except ValueError as e:
            print(e)

    def try_load_workbook(self):
        try:
            workbook = load_workbook(language.read_file()['path_to_xlsx'])
        except InvalidFileException:
            print("we need xlsx file!")
            return
        except KeyError:
            print("please check xlsx format file!")
            return
        except FileNotFoundError:
            print("file missing :D")
            return
        return workbook