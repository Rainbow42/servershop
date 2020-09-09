import sys
import requests
from config import FILE_HTML, FILE_NAME_JSON, HEADERS, FILE_NAME_JSON_SPECIFICATIONS
from datebase.db import Database
from parse.url import Date
from parse.parse import Parse
from servers.send import Send
from multiprocessing import Process


def input_link():
    message = input("Please enter a link to the list of products")
    return message


def get(url):
    session = requests.Session()
    link = Date()
    html, status_code = link.get(filename=FILE_HTML,
                                 url=url,
                                 session=session,
                                 headers=HEADERS)
    return html, status_code


def main():
    url = ' '.join(sys.argv[1:]) or ''  # получение данных с терминала

    while True:
        if url:
            date_json = []
            html, status_code = get(url)
            # print(html)
            if status_code == 200:
                date = Parse()
                page = date.number_page(text=html)  # подсчет колличества страниц
                for itm in range(1, page + 1):
                    url += '?available=1&status=55395790&p=' + str(itm)
                    print('url = {}  Page {}'.format(url, itm))
                    html, status_code = get(url)
                    if status_code == 200:
                        date_json.append(date.search(text=html,
                                                     filename=FILE_NAME_JSON))
                send = Process(target=Send, args=(date_json,))
                send.start()
                send.join()
                db = Database()
                db.read_file_json(FILE_NAME_JSON_SPECIFICATIONS)
            url = ''
        else:
            url = input_link()


if __name__ == '__main__':
    main()
