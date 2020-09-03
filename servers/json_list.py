import json
"""MESSAGE = [{"name": "Ноутбук ACER Aspire 1 A114-32-C4F6, NX.GW9ER.004, синий", "price": "18990руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1194642/"},
           {"name": "Ноутбук LENOVO IdeaPad S340-14API, 81NB006VRK, серый", "price": "39990руб.39890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1153686/"},
           {"name": "Ультрабук HONOR MagicBook 14 Nbl-WAQ9HNR, 53010TPS, серый", "price": "44670руб.43820руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1367774/"},
           {"name": "Ноутбук LENOVO IdeaPad S145-15API, 81UT00FDRU, серый", "price": "46990руб.46890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1214764/"},
           {"name": "Ноутбук LENOVO IdeaPad S340-15API, 81NC009LRK, серый", "price": "34990руб.34890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1154363/"},
           {"name": "Ноутбук MSI GF63 Thin 9RCX-683XRU, 9S7-16R312-683, черный", "price": "68990руб.68890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1167101/"},
           {"name": "Ноутбук LENOVO IdeaPad L340-15IRH, 81LK01E6RK, черный", "price": "61990руб.61890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1216438/"},
           {"name": "Ноутбук LENOVO IdeaPad S145-15AST, 81N3008LRU, черный", "price": "34990руб.34890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1154183/"},
           {"name": "Ноутбук LENOVO IdeaPad S145-15IIL, 81W8001RRK, серый", "price": "39990руб.39890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1193897/"},
           {"name": "Ноутбук LENOVO IdeaPad S145-15API, 81UT00AYRU, серый", "price": "34990руб.34890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1193891/"},
           {"name": "Ноутбук MSI GF63 Thin 9RCX-685XRU, 9S7-16R312-685, черный", "price": "62990руб.62890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1167106/"},
           {"name": "Ноутбук ACER Aspire 3 A315-42-R2SE, NX.HF9ER.02S, черный", "price": "49990руб.49890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1170053/"},
           {"name": "Ноутбук LENOVO IdeaPad S145-15API, 81UT007GRU, черный", "price": "43990руб.43890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1175132/"},
           {"name": "Ноутбук LENOVO IdeaPad S340-15API, 81NC00JCRU, серый", "price": "35490руб.35090руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1214772/"},
           {"name": "Ноутбук LENOVO IdeaPad S145-15AST, 81N300EWRU, черный", "price": "34990руб.34890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1193896/"},
           {"name": "Ноутбук ACER Aspire 7 A715-75G-51FE, NH.Q87ER.002, черный", "price": "59990руб.59890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1217408/"},
           {"name": "Ноутбук LENOVO Legion Y540-15PG0, 81SY00KNRK, черный", "price": "74490руб.73690руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1201141/"},
           {"name": "Ноутбук ASUS M509DJ-BQ078, 90NB0P22-M01040, серый", "price": "39990руб.39890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1198296/"},
           {"name": "Ноутбук ACER Aspire 7 A715-75G-56ZT, NH.Q88ER.002, черный", "price": "65990руб.65890руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1217407/"},
           {"name": "Ноутбук HUAWEI MateBook D 14 Nbl-WAQ9R, 53010TTB, серый", "price": "42990руб.47690руб.",
            "url": "https://www.citilink.ru/catalog/mobile/notebooks/1372334/"}]"""


def read_file(filename):
    with open('url_list.json') as input_file:
        data = json.load(input_file)  # загружаем из файла данные в словарь data
        input_file.close()
    return data


MESSAGE = (read_file('url_list.json'))

url_list = []
for i in MESSAGE:
    url_list.append(i['url'])
print(url_list)
