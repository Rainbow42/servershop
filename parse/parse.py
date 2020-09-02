from lxml import html
from bs4 import BeautifulSoup
import requests
import csv


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def anser_file(filename, list):
    with open(filename, "w", newline="") as file:
        for item in list:
            file.write(str(item)+'\n')


class Date:

    def get(self, url, session):
        request = session.get(url)
        print("Answer {}".format(request))
        with open('test.html', 'w') as output_file:
            output_file.write(str(request.text))
        return request.text


class Parse:
    def search(self, text):
        soup = BeautifulSoup(text, 'lxml')
        technical = soup.find('div', {'class': 'product_category_list'})
        prices = technical.find_all('div', {'class': 'subcategory-product-item__price-container'})
        technicals = technical.find_all('a', {'class': 'link_gtm-js link_pageevents-js ddl_product_link'})
        technical_lists = []
        if len(prices) == len(technicals):
            for technical in range(len(technicals)):
                technical_link = technicals[technical].get('href')
                technical_desc = technicals[technical].text.strip()
                price = prices[technical].text.replace("\n ", "").replace(" ", "")
                technical_lists.append({'name': technical_desc,
                                        'price': price,
                                        'url': technical_link,
                                        })
        else:
            technical_list.append('Error len')
        return technical_lists


s = requests.Session()
url = Date()
html = url.get(url='https://www.citilink.ru/catalog/mobile/notebooks/', session=s)
date = Parse()
technical_list = date.search(read_file('test.html'))
anser_file("otput.txt", technical_list)
print(technical_list)
