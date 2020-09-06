from bs4 import BeautifulSoup
import json
from work_file import json_file


class Parse:
    def search(self, text, filename):
        """Метод для поулчения полной информации по конкретному товару"""
        soup = BeautifulSoup(text, 'lxml')
        try:
            data = []
            table = soup.find('table', {'class': 'product_features'})  # парсинг общих характеристик в таблице
            table_body = table.find_all('tr')
            for row in table_body:
                title_span = ""
                titles = row.find_all('span', {'class': 'property_name'})
                for span in titles: #  работы с тегами таблицы
                    title_span = span.string
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                for ele in cols:
                    if ele and title_span:
                        data.append({str(title_span): str(ele)})
            div = soup.find('div', {'class': 'specification_view product_view'})  # парсинг общего опсиания товара
            div_list = div.find('div').find('li').find_all('meta')
            description = []  # описание
            for i in div_list:  # получение общего описания товара
                description.append(
                    i['content'].replace('<p>', '').replace('</p>', '').replace('.&nbsp;Smart&nbsp;', ''). \
                        replace('\n', ''). \
                        replace('&nbsp;', ''). \
                        replace('/n-', '').replace("\\/", "/"))
            # добавление общего описания товара к характерискам
            data.append({'Наименование товара': description[0], 'Описание товара': ''.join(description[1:])})
            json_file(filename=filename,
                      list=data)
            # возвращаем полную информацуию о товаре
            return json.dumps(data).replace("\\/", "/").encode().decode('unicode_escape')
        except Exception as err:
            return str(err)
