from bs4 import BeautifulSoup
from work_file import json_file


class Parse:

    def search(self, text, filename):
        soup = BeautifulSoup(text, 'lxml')
        try:
            technical = soup.find('div', {'class': 'product_category_list'})
            prices = technical.find_all('div', {'class': 'subcategory-product-item__price-container'})
            technicals = technical.find_all('a', {'class': 'link_gtm-js link_pageevents-js ddl_product_link'})
            page_number = soup.find('div', {'class': 'main_content'})
            page_number = soup.find('div', {'class': 'page_listing'}).find('ul').find_all('li').find_all('a')
            print(page_number)
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
                json_file(filename=filename,
                          list=technical_lists)
            else:
                technical_lists.append('Error len')
        except:
            return f'Error url!'
