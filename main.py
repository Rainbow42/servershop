import sys
import requests
from config import FILE_HTML, FILE_NAME_JSON, HEADERS
from parse.url import Date
from parse.parse import Parse
from servers.send import Send
from servers.worker import Worker
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
            work = Process(target=Worker)  # созаднеи прослушки канала

            date_json = []
            html, status_code = get(url)
            # print(html)
            if status_code == 200:
                date = Parse()
                page = date.number_page(text=html)
                # print('Count page {}'.format(page))
                for itm in range(1, page + 1):
                    url += '?available=1&status=55395790&p=' + str(itm)
                    print('url = {}  Page {}'.format(url, page))
                    html, status_code = get(url)
                    if status_code == 200:
                        date_json.append(date.search(text=html,
                                                     filename=FILE_NAME_JSON))
                #work.close()
                #print(date_json)
                send = Process(target=Send, args=(date_json,))
                work.start()
                send.start()
            url = ''
        else:
            url = input_link()


if __name__ == '__main__':
    main()
