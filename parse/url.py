import requests


class Date:

    def get(self, url, session):
        r = requests.get(url)
        print("Answer {}".format(r))
        request = session.get(url)
        with open('test.html', 'w') as output_file:
            output_file.write(str(r.text.encode('utf-8')))
        return request.text


s = requests.Session()
url = Date()
url.get(url='https://www.citilink.ru/catalog/mobile/smartfony/', session=s)
