import sys
import requests
from config import FILE_HTML, FILE_NAME_JSON
from parse.url import Date
from parse.parse import Parse, read_file
from servers.send import Send
message = ' '.join(sys.argv[1:]) or " "

s = requests.Session()
url = Date()
html = url.get(filename=FILE_HTML,
               url=message,
               session=s)

date = Parse()
technical_list = date.search(text=read_file(FILE_HTML),
                             filename=FILE_NAME_JSON)
Send()


