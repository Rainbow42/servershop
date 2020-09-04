import sys
import requests
from config import FILE_HTML, FILE_NAME_JSON
from parse.url import Date
from parse.parse import Parse
from servers.send import Send
from work_file import read_file
import threading


message = ' '.join(sys.argv[1:]) or " "


s = requests.Session()
url = Date()
html = url.get(filename=FILE_HTML,
               url=message,
               session=s)

if not ('Submission link' in html or 'Error url' in html):
    date = Parse()
    technical_list = date.search(text=read_file(FILE_HTML),
                                 filename=FILE_NAME_JSON)

    Send()

else:
    print(html)
