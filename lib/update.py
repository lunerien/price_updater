from openpyxl import load_workbook
from bs4 import BeautifulSoup
from requests import get, exceptions, get
from openpyxl.utils.exceptions import InvalidFileException
from typing import Tuple

from lib.language import language
from lib.currency import currency, Currency
from lib.asset import Asset


class Update:
    def __init__(self):
        self.workbook = self.try_load_workbook()
        self.dec: int = 3

    def update(self, coins):
        if self.workbook != None:
            data = self.workbook["data"]
            i = 1
            while data.cell(row=1, column=i).value != None:
                if data.cell(row=1, column=i).value != "-":
                    price = next(
                        self.get_price(coin)
                        for coin in coins
                        if coin.name == data.cell(row=1, column=i).value
                    )
                    sheet = self.workbook[data.cell(row=2, column=i).value]
                    if price != "0,0":
                        print(price)
                        sheet[data.cell(row=3, column=i).value] = price
                i += 1
            self.workbook.save(language.read_file()["path_to_xlsx"])

    def get_price(self, coin: Asset):
        match coin.chosen_currency:
            case Currency.USD:
                return coin.price_usd
            case Currency.PLN:
                return coin.price_pln
            case Currency.EUR:
                return coin.price_eur
            case Currency.GBP:
                return coin.price_gbp

    def get_asset_price(self, ticker: str):
        fiat_assets: Tuple[str, ...] = ("eur", "gbp", "usd")
        metal_assets: Tuple[str, ...] = ("gold", "silver")
        etf_assets: Tuple[str, ...] = ("swda-etf", "emim-etf")

        if ticker in fiat_assets:
            return self.get_fiat_price(ticker)
        elif ticker in metal_assets:
            return self.get_metal_price(ticker)
        elif ticker in etf_assets:
            return self.get_etf_price(ticker)
        else:
            return self.get_crypto_price(ticker)

    def try_load_workbook(self):
        try:
            workbook = load_workbook(language.read_file()["path_to_xlsx"])
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

    def _exception_catch(self, e):
        if isinstance(e, exceptions.ConnectionError):
            currency.connection_lost = True
        return {
            Currency.USD: "0,0",
            Currency.PLN: "0,0",
            Currency.EUR: "0,0",
            Currency.GBP: "0,0",
            "asset_logo": None
        }

    def get_fiat_price(self, ticker):
        try:
            match (ticker):
                case "usd":
                    return {
                        Currency.USD: "1,0",
                        Currency.PLN: str(currency.usd_pln).replace(".", ","),
                        Currency.EUR: str(
                            round(currency.usd_pln / currency.eur_pln, self.dec)
                        ).replace(".", ","),
                        Currency.GBP: str(
                            round(currency.usd_pln / currency.gbp_pln, self.dec)
                        ).replace(".", ","),
                        "asset_logo": f"./images/asset_logo/{ticker}.png"
                    }
                case "gbp":
                    return {
                        Currency.USD: str(
                            round(currency.gbp_pln / currency.usd_pln, self.dec)
                        ).replace(".", ","),
                        Currency.PLN: str(currency.gbp_pln).replace(".", ","),
                        Currency.EUR: str(
                            round(currency.gbp_pln / currency.eur_pln, self.dec)
                        ).replace(".", ","),
                        Currency.GBP: "1,0",
                        "asset_logo": f"./images/asset_logo/{ticker}.png"
                    }
                case "eur":
                    return {
                        Currency.USD: str(
                            round(currency.eur_pln / currency.usd_pln, self.dec)
                        ).replace(".", ","),
                        Currency.PLN: str(currency.eur_pln).replace(".", ","),
                        Currency.EUR: "1,0",
                        Currency.GBP: str(
                            round(currency.eur_pln / currency.gbp_pln, self.dec)
                        ).replace(".", ","),
                        "asset_logo": f"./images/asset_logo/{ticker}.png"
                    }
        except:
            {
                Currency.USD: "0,0",
                Currency.PLN: "0,0",
                Currency.EUR: "0,0",
                Currency.GBP: "0,0",
                "asset_logo": f"./images/asset_logo/{ticker}.png"
            }

    def get_metal_price(self, ticker):
        def get_price() -> float:
            try:
                url = f"https://www.kitco.com/charts/live{ticker}.html"
                page = get(url)
                bs = BeautifulSoup(page.content, "html.parser")

                for nastronie in bs.find_all("div", class_="data-blk bid"):
                    price = nastronie.find("span").get_text()
                    price = price.replace(",", "")
                    return float(price)
            except (
                ValueError,
                ZeroDivisionError,
                TypeError,
                exceptions.ConnectionError,
            ) as e:
                value = self._exception_catch(e)
                return value
            return 0.0

        price_exact = get_price()
        try:
            return {
                Currency.USD: str(price_exact).replace(".", ","),
                Currency.PLN: str(
                    round(price_exact * currency.usd_pln, self.dec)
                ).replace(".", ","),
                Currency.EUR: str(
                    round(price_exact * (currency.usd_pln / currency.eur_pln), self.dec)
                ).replace(".", ","),
                Currency.GBP: str(
                    round(price_exact * (currency.usd_pln / currency.gbp_pln), self.dec)
                ).replace(".", ","),
                "asset_logo": f"./images/asset_logo/{ticker}.png"
            }
        except:
            return (
                {
                    Currency.USD: "0,0",
                    Currency.PLN: "0,0",
                    Currency.EUR: "0,0",
                    Currency.GBP: "0,0",
                    "asset_logo": f"./images/asset_logo/{ticker}.png"
                },
            )

    def get_etf_price(self, ticker):
        link: str
        if ticker == "swda-etf":
            link = "https://www.hl.co.uk/shares/shares-search-results/i/ishares-core-msci-world-ucits-etf-usd-acc"
        else:
            link = "https://www.hl.co.uk/shares/shares-search-results/i/ishares-core-msci-emerging-markets-imi-ucit"

        def get_price() -> float:
            try:
                page = get(link)
                bs = BeautifulSoup(page.content, "html.parser")
                for onpage in bs.find("span", class_="bid price-divide"):
                    page_str = str(onpage)
                    page_str = page_str.replace("p", "")
                    page_str = page_str.replace(",", "")
                    price = page_str[0:4]
                    return float(price)
            except (
                ValueError,
                ZeroDivisionError,
                TypeError,
                exceptions.ConnectionError,
            ) as e:
                value = self._exception_catch(e)
                return value
            return 0.0

        price_exact = get_price()
        try:
            return {
                Currency.USD: str(
                    round(price_exact * (currency.gbp_pln / currency.usd_pln), self.dec)
                ).replace(".", ","),
                Currency.PLN: str(
                    round(price_exact * currency.gbp_pln, self.dec)
                ).replace(".", ","),
                Currency.EUR: str(
                    round(price_exact * (currency.gbp_pln / currency.eur_pln), self.dec)
                ).replace(".", ","),
                Currency.GBP: str(price_exact).replace(".", ","),
                "asset_logo": f"./images/asset_logo/ishares.png"
            }
        except:
            return {
                Currency.USD: "0,0",
                Currency.PLN: "0,0",
                Currency.EUR: "0,0",
                Currency.GBP: "0,0",
                "asset_logo": f"./images/asset_logo/ishares.png"
            }

    def get_crypto_price(self, ticker):
        try:
            url = f"https://coinmarketcap.com/currencies/{ticker.lower()}"
            page = get(url)
            bs = BeautifulSoup(page.content, "html.parser")

            data = bs.find('div', class_="sc-16891c57-0 gYEgxU")
            raw_data = data.find("img", src=True)
            http_logo: str= raw_data['src']

            for web in bs.find_all(
                "div",
                class_="sc-16891c57-0 hqcKQB flexStart alignBaseline",
            ):
                price_str = str(
                    web.find("span", class_="sc-16891c57-0 dxubiK base-text")
                )
                price_str = price_str.replace(
                    '<span class="sc-16891c57-0 dxubiK base-text">$', ""
                )
                price_str = price_str.replace("</span>", "")
                price_str = price_str.replace(",", "")
                price_float = float(price_str)
                ######################################################
                price_usd = (
                    str(round(price_float, 6))
                    if price_str[:2] == "0."
                    else str(round(price_float, 2))
                )
                price_usd = price_usd.replace(".", ",")
                ######################################################
                price_pln_float = price_float * currency.return_price(Currency.USD)
                price_pln = (
                    str(round(price_pln_float, 6))
                    if price_str[:2] == "0."
                    else str(round(price_pln_float, 2))
                )
                price_pln = price_pln.replace(".", ",")
                ######################################################
                price_eur_float = price_float * (
                    currency.return_price(Currency.USD)
                    / currency.return_price(Currency.EUR)
                )
                price_eur = (
                    str(round(price_eur_float, 6))
                    if price_str[:2] == "0."
                    else str(round(price_eur_float, 2))
                )
                price_eur = price_eur.replace(".", ",")
                ######################################################
                price_gbp_float = price_float * (
                    currency.return_price(Currency.USD)
                    / currency.return_price(Currency.GBP)
                )
                price_gbp = (
                    str(round(price_gbp_float, 6))
                    if price_str[:2] == "0."
                    else str(round(price_gbp_float, 2))
                )
                price_gbp = price_gbp.replace(".", ",")
                ######################################################
                return {
                    Currency.USD: price_usd,
                    Currency.PLN: price_pln,
                    Currency.EUR: price_eur,
                    Currency.GBP: price_gbp,
                    "asset_logo": http_logo
                }
        except (
            ValueError,
            ZeroDivisionError,
            TypeError,
            exceptions.ConnectionError,
        ) as e:
            value = self._exception_catch(e)
            return value
