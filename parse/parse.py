from bs4 import BeautifulSoup
from work_file import json_file


class Parse:
    def number_page(self, text):
        try:
            soup = BeautifulSoup(text, 'lxml')
            page = soup.find('div', {'class': 'main_content'}).find('div', {'class': 'main_content_wrapper'})
            page = page.find('div', {'id': 'subcategoryList'}).find('div', {'class': 'page_listing'})
            last = page.find('li', {'class': 'last'})
            if last is None:
                pages = page.find_all('li', {'class': 'next'})
                for itm in pages:
                    page = int(itm.text.replace(' ', ''))
                return page
            else:
                for itm in last:
                    page = itm
                return int(itm.text.replace(' ', ''))
        except Exception as err:
            print(err)
            return 1

    def search(self, text, filename):
        """Поиск товаров по полченной странице"""

        soup = BeautifulSoup(text, 'lxml')
        try:
            technical = soup.find('div', {'class': 'product_category_list'})
            prices = technical.find_all('div', {'class': 'subcategory-product-item__price-container'})
            technicals = technical.find_all('a', {'class': 'link_gtm-js link_pageevents-js ddl_product_link'})
            technical_lists = []
            if len(prices) == len(technicals):  # проверка количесва товара на станице по списку цен
                for technical in range(len(technicals)):  # парсинг страницы
                    technical_link = technicals[technical].get('href')
                    technical_desc = technicals[technical].text.strip()
                    price = prices[technical].text.replace("\n ", "").replace(" ", "")
                    technical_lists.append({'name': technical_desc,
                                            'price': price,
                                            'url': technical_link,
                                            })
                # print((technical_lists))
                json_file(filename=filename,
                          list=technical_lists)

                return list(technical_lists)
            else:
                technical_lists.append('Error len!')  # если проверка не прошла возврашаем текст ошибки
        except Exception as err:
            return f'Error parse page!' + str(err)
