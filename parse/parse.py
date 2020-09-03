from conf import *
from bs4 import BeautifulSoup
import json


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
        input_file.close()
    return text


def json_file(filename, list):
    app_json = json.dumps(list)
    with open(filename, "w", newline="") as file:
        file.write(app_json.replace("\\/", "/").encode().decode('unicode_escape'))
    file.close()


class Parse:

    def search(self, text):
        soup = BeautifulSoup(text, 'lxml')
        try:
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
                technical_lists.append('Error len')
            json_file(filename=FILE_NAME_JSON,
                      list=technical_lists)
        except:
            return f'Error url!'
