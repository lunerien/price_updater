from openpyxl import load_workbook
from bs4 import BeautifulSoup
from requests import get
from openpyxl.utils.exceptions import InvalidFileException

from lib.language import language
from lib.currency import currency, Currency
from lib.asset import Asset

class Update:
    def __init__(self):
        self.workbook = self.try_load_workbook()
    
    def update(self, coins):
        if self.workbook != None:
            data = self.workbook['data']
            i = 1
            while data.cell(row=1, column=i).value != None:
                if data.cell(row=1, column=i).value != "-":
                    price = next(self.get_price(coin) for coin in coins if coin.name == data.cell(row=1, column=i).value)
                    sheet = self.workbook[data.cell(row=2, column=i).value]
                    print(price)
                    sheet[data.cell(row=3, column=i).value] = price
                i += 1
            self.workbook.save(language.read_file()['path_to_xlsx'])

    def get_price(self, coin:Asset):
        match coin.chosen_currency:
            case Currency.USD:
                return coin.price_usd
            case Currency.PLN:
                return coin.price_pln
            case Currency.EUR:
                return coin.price_eur
            case Currency.GBP:
                return coin.price_gbp

    def get_asset_price(self, ticker:str):
        other_coins: str = ('eur', 'gbp', 'usd')

        if ticker in other_coins:
            match(ticker):
                case 'usd':
                    return {Currency.USD: '1,0', Currency.PLN: str(currency.usd_pln).replace('.', ','), Currency.EUR: str(currency.usd_pln/currency.eur_pln).replace('.', ','), Currency.GBP: str(currency.usd_pln/currency.gbp_pln).replace('.', ',')}
                case 'gbp':
                    return {Currency.USD: '0,0', Currency.PLN: str(currency.gbp_pln).replace('.', ','), Currency.EUR: '0,0', Currency.GBP: '1,0'}
                case 'eur':
                    return {Currency.USD: '0,0', Currency.PLN: str(currency.eur_pln).replace('.', ','), Currency.EUR: '1,0', Currency.GBP: '0,0'}
                    
        else:
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
                    ######################################################
                    price_usd = str(round(price_float, 6)) if price_str[:2] == "0." else str(round(price_float, 2))
                    price_usd = price_usd.replace(".", ",")
                    ######################################################
                    price_pln_float = price_float * currency.return_price(Currency.USD)
                    price_pln = str(round(price_pln_float, 6)) if price_str[:2] == "0." else str(round(price_pln_float, 2))
                    price_pln = price_pln.replace(".", ",")
                    ######################################################
                    price_eur_float = price_float * (currency.return_price(Currency.USD) / currency.return_price(Currency.EUR))
                    price_eur = str(round(price_eur_float, 6)) if price_str[:2] == "0." else str(round(price_eur_float, 2))
                    price_eur = price_eur.replace(".", ",")
                    ######################################################
                    price_gbp_float = price_float * (currency.return_price(Currency.USD) / currency.return_price(Currency.GBP))
                    price_gbp = str(round(price_gbp_float, 6)) if price_str[:2] == "0." else str(round(price_gbp_float, 2))
                    price_gbp = price_gbp.replace(".", ",")
                    ######################################################
                    return {Currency.USD: price_usd, Currency.PLN: price_pln, Currency.EUR: price_eur, Currency.GBP: price_gbp}
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