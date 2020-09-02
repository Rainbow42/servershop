from lxml import html
from bs4 import BeautifulSoup
import requests
from servershop.parse.url import Date


class Parse:
    pass


s = requests.Session()
url = Date()
url.get(url='https://www.citilink.ru/catalog/mobile/smartfony/', session=s)
