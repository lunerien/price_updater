from openpyxl import load_workbook
from bs4 import BeautifulSoup
from requests import get

from lib.language import language


class Update:
    def __init__(self):
        self.workbook = load_workbook(language.read_file()['path_to_xlsx'])
    
    def update(self):
        data = self.workbook['data']

        i = 1
        while data.cell(row=1, column=i).value != None:
            if data.cell(row=1, column=i).value != "-":
                print(data.cell(row=1, column=i).value)
                print(data.cell(row=2, column=i).value)
                print(data.cell(row=3, column=i).value)
                price = self.get_token_price(data.cell(row=1, column=i).value)
                sheet = self.workbook[data.cell(row=2, column=i).value]
                sheet[data.cell(row=3, column=i).value] = price
            i += 1
        self.workbook.save(language.read_file()['path_to_xlsx'])

    def get_token_price(self, ticker:str):
        url = f"https://www.coingecko.com/pl/waluty/{ticker}"
        page = get(url)
        bs = BeautifulSoup(page.content, "html.parser")

        for nastronie in bs.find_all(
            "td",
            class_="border-top-0 tw-text-right tw-text-sm tw-border-gray-200 dark:tw-border-opacity-10",
        ):
            price = str(nastronie.find("span", class_="no-wrap"))
            price = price.split("$", 1)[-1]
            price = price.replace("</span>", "")
            price = price.replace(" ", "")
            return price
