import sys
import requests
from config import FILE_HTML, FILE_NAME_JSON
from parse.url import Date
from parse.parse import Parse
from servers.send import Send
from servers.worker import Worker
from work_file import read_file
from multiprocessing import Process


def input_link():
    message = input("Please enter the link ")
    return message


def main():
    work = Process(target=Worker)
    work.start()
    message = ' '.join(sys.argv[1:]) or ''
    while True:
        print(message)
        session = requests.Session()
        url = Date()
        html = url.get(filename=FILE_HTML,
                       url=message,
                       session=session)
        if message:
            if not ('Submission link' in html or 'Error url' in html):
                date = Parse()
                date.search(text=read_file(FILE_HTML),
                            filename=FILE_NAME_JSON)
                send = Process(target=Send())
                send.start()
            else:
                print(html)
                message = input_link()
        else:
            message = input_link()


if __name__ == '__main__':
    main()
