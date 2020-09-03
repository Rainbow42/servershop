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

    def search(self, text, filename):
        soup = BeautifulSoup(text, 'lxml')
        try:
            print('HEll')
            data = []
            table = soup.find('table', {'class': 'product_features'})
            table_body = table.find_all('tr')
            # print(table_body)

            for row in table_body:
                title_span = ""
                titles = row.find_all('span', {'class': 'property_name'})
                for span in titles:
                    title_span = span.string
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                for ele in cols:
                    if ele and title_span:
                        data.append({title_span: ele})
                print(data)
                # data.append([ele for ele in cols if ele])

            """prices = technical.find_all('div', {'class': 'subcategory-product-item__price-container'})
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
            json_file(filename=filename,
                      list=technical_lists)"""
        except:
            return f'Error url!'
