import sys
import requests
from conf import TEST_URL, FILE_HTML
from parse.url import Date
from parse.parse import Parse, read_file

message = ' '.join(sys.argv[1:]) or " "

s = requests.Session()
url = Date()
html = url.get(filename=FILE_HTML,
               url=message,
               session=s)

date = Parse()
technical_list = date.search(read_file(FILE_HTML))
print(technical_list)
