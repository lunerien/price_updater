from openpyxl import load_workbook
from bs4 import BeautifulSoup
from requests import get
from openpyxl.utils.exceptions import InvalidFileException

from lib.language import language
from lib.currency import currency, Currency

class Update:
    def __init__(self):
        self.workbook = self.try_load_workbook()
    
    def update(self, coins):
        if self.workbook != None:
            data = self.workbook['data']

            i = 1
            while data.cell(row=1, column=i).value != None:
                if data.cell(row=1, column=i).value != "-":
                    price = next(coin.price for coin in coins if coin.name == data.cell(row=1, column=i).value)
                    print(price)
                    sheet = self.workbook[data.cell(row=2, column=i).value]
                    sheet[data.cell(row=3, column=i).value] = price
                i += 1
            self.workbook.save(language.read_file()['path_to_xlsx'])

    def get_token_price(self, ticker:str):
        url = f"https://www.coingecko.com/pl/waluty/{ticker.lower()}"
        page = get(url)
        bs = BeautifulSoup(page.content, "html.parser")

        for web in bs.find_all(
            "td",
            class_="border-top-0 tw-text-right tw-text-sm tw-border-gray-200 dark:tw-border-opacity-10",
        ):
            price_str = str(web.find("span", class_="no-wrap"))
            price_str = price_str.split("$", 1)[-1]
            price_str = price_str.replace("</span>", "")
            price_str = price_str.replace(" ", "")
            price_str = price_str.replace(",", ".")
            price_float = float(price_str)

            price_usd = str(round(price_float, 6)) if price_str[:2] == "0." else str(round(price_float, 2))
            price_usd = price_usd.replace(".", ",")

            price_pln_float = price_float * currency.return_price(Currency.PLN)
            price_pln = str(round(price_pln_float, 6)) if price_str[:2] == "0." else str(round(price_pln_float, 2))
            price_pln = price_pln.replace(".", ",")

            return {Currency.USD: price_usd, Currency.PLN: price_pln}

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