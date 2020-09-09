import sys

sys.path.append('../')
FILE_NAME_JSON = 'servers/ url_list.json'
TEST_URL = 'https://www.citilink.ru/catalog/mobile/notebooks/'
FILE_HTML = 'test.html'
FILE_HTML_SPECIFICATIONS = 'test2.html'
FILE_NAME_JSON_SPECIFICATIONS = 'url_list2.json'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.86 '
                  'YaBrowser/20.8.0.864 (beta) Yowser/2.5 Safari/537.36',
    'accet': '*/*'}

COUNT_THREAD = 5
