import psycopg2
# from work_file import read_file_json
from googletrans import Translator
# from config import FILE_NAME_JSON_SPECIFICATIONS
import json

from psycopg2 import sql

FILE_NAME_JSON_SPECIFICATIONS = 'url_list2.json'

conn = psycopg2.connect(database="citilink", user="antonida",
                        password="password", host="localhost", port=5432)
cur = conn.cursor()


def create_table(description, title):
    stroka = "CREATE TABLE " + str(title) + " (id SERIAL PRIMARY KEY "
    for i in range(len(description)):
        if i != len(description):
            stroka += ", " + str(description[i]).lower() + " VARCHAR"
    stroka += " );"
    print(stroka)
    return stroka


def insert_table(data_json, title, description):
    insert = []
    values = [
        ('ALA', 'Almaty', 'Kazakhstan'),
        ('TSE', 'Astana', 'Kazakhstan'),
        ('PDX', 'Portland', 'USA'),
    ]
    # inserts = cur.execute('INSERT INTO {} (code, name, country_name) VALUES {}'.format(title))
    for i in data_json:
        for x in i:
            if 'Наименование товара' in x.keys():
                name = x['Наименование товара'].split(' ')[0]
                insert.append([name])
                # print(name)
        break
    count = 0
    for i in data_json:
        if count < len(data_json):
            for x in i:
                if not 'Наименование товара' in x.keys():
                    string = str(list(x.values())[0])
                    insert[count].append(string)

        count += 1
        break
    list_tuple = []
    for i in insert:
        list_tuple.append(tuple(i))
    # print(list_tuple)
    string = ""
    for i in description:
        string += i + ', '
    #print(string.lower())
    print(title)
    title = "INSERT INTO " + str(title)
    inserts = sql.SQL(title + " ({}) VALUES {}".format(string.lower(), list_tuple))
    print(insert)
    cur.execute(insert)
    print(cur.fetchall())

def read_file_json(filename):
    with open(filename) as input_file:
        data = json.load(input_file)
        input_file.close()
    return data


data_json = [{'Совместимость с брендом': 'Canon'},
             {'Ведущее число макс(ISO100)': '43 м'}, {'Зум, нижняя граница': '24 мм'},
             {'Зум, верхняя граница': '105 мм'}, {'FP-синхронизация': 'ДА'}, {'Синхронизация по второй шторке': 'ДА'},
             {'Наклон вверх': '90 °'}, {'Наклон вправо': '180 °'}, {'Наклон влево': '150 °'},
             {'Контроль цветовой температуры': 'ДА'}, {'Возможность беспроводного управления': 'ДА'},
             {'Коммерческое название основной системы экспозамера': 'E-TTLII'}, {'Подсветка автофокуса': 'ДА'},
             {'Стробоскопический режим': 'ДА'}, {'Минимальное время перезарядки': '3.5 с'},
             {'Элемент питания, тип': 'AA'}, {'Элемент питания, кол-во': '4'}, {'Вес без батарей': '295 г'},
             {'Гарантия': '12 мес.'}, {'Страна производитель': 'Тайвань (Китай)'},
             {'Наименование товара': 'Вспышка CANON Speedlight 430EX III -RT'}, {
                 'Описание товара': 'Универсальная вспышка CANON Speedlight 430EX III-RT является устройством для '
                                    'создания лучших фотографий. Ведущее число равно 43 м. Этого хватает для съемки '
                                    'со вспышкой на небольшой дистанции. Имеется автоматический зум для изменения '
                                    'угла освещения. Поворотная головка обеспечивает более мягкую подсветку без '
                                    'резких теней.Мощность вспышки CANON Speedlight 430EX III-RT вы можете '
                                    'подстраивать под себя от 1:1 до 1:64. Горизонтально устройство поворачивается на '
                                    '270 градусов, а вертикально на 45, 60, 75 и 90 градусов. Также возможна работа '
                                    'на дистанции с фотоаппаратом. Предусмотрена FP-синхронизация для эффективной '
                                    'работы с тенями. Питание осуществляется от 4 батареек типа АА.'},
             {'url': b'https://www.citilink.ru/catalog/photo_and_video/photo_flashes/346629/'}], \
            [{'Совместимость с '
              'брендом': 'Nikon'}, {'Ведущее число макс(ISO100)': '24 м'},
             {'FP-синхронизация': 'Да'}, {'Синхронизация по второй шторке': 'Да'},
             {'Наклон вверх': '90 °'}, {'Наклон вправо': '180 °'},
             {'Наклон влево': '180 °'},
             {'Возможность беспроводного управления': 'Да'},
             {'Коммерческое название основной системы экспозамера': 'i-TTL'}, {'Подсветка автофокуса': 'Да'},
             {'Элемент питания, тип': 'AA'}, {'Элемент питания, кол-во': '2'}, {'Вес без батарей': '226 г'},
             {'Гарантия': '24 мес.'}, {'Страна производитель': 'Китай'},
             {'Наименование товара': 'Вспышка NIKON Speedlight SB-500'}, {
                 'Описание товара': 'Практичная вспышка NIKON Speedlight SB-500 станет верным помощником всем '
                                    'фотографам, которые желают получать качественные снимки при любом освещении. '
                                    'Совмещается с устройствами компании Nikon линейки Coolpix. Перезарядка '
                                    'происходит за три с половиной секунды. Длительность свечения равна 1 на 650 '
                                    'секунд, поэтому работать с короткими выдержками значительно проще.У поворотной '
                                    'головки вспышки NIKON Speedlight SB-500 имеется три угла наклона&#151; 60, '
                                    '75 и 90 градусов, поэтому вы сможете настроить свет так, как вам нужно. '
                                    'Совместима модель с i-TTL. Простое управление делает работу с устройством '
                                    'приятной и комфортной. Вспышка работает от двух батареек типа ААА.'},
             {'url': b'https://www.citilink.ru/catalog/photo_and_video/photo_flashes/998318/'}]
translator = Translator()
title = ''
name = ''
description = []
for i in data_json:
    for x in i:
        if 'Наименование товара' in x.keys():
            keys = str(list(x.keys())[0])
            title = x['Наименование товара'].split(' ')[0]
            # print(title)
            result = translator.translate(keys, src='ru')
            description.append(result.text.replace(" ", "_"))
            name = translator.translate(title, src='ru')
            name = name.text.lower()
            # print(result.text)
    break
for i in data_json:
    for x in i:
        if not 'Наименование товара' in x.keys():
            r = translator.translate(str(list(x.keys())[0]), src='ru')
            r = r.text.replace(",", "").replace(' ', "_").replace('(', "").replace(")", "")
            description.append(r)
    break
# print(description)


check_create = cur.execute(
    "SELECT n.nspname, c.relname FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace WHERE c.relkind = 'r' AND n.nspname NOT IN('pg_catalog', 'citilink');")
list_table = cur.fetchall()
for itm in list_table:
    if name in itm[1]:
        insert_table(data_json, name, description)
