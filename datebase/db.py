import psycopg2
# from work_file import read_file_json
from googletrans import Translator
import json

from psycopg2 import sql


class Database:
    def __init__(self):
        self.translator = Translator()
        self.conn = psycopg2.connect(database="citilink", user="antonida",
                                     password="password", host="localhost", port=5432)
        self.cur = self.conn.cursor()

    def data_validation(self, select_list, data_list) -> list:
        """Проверка на совпадение данных из бд и новых данных."""
        res = []
        # print(select_list)
        for select in select_list:
            for index, tuples in enumerate(data_list):
                for s in range(len(select)):
                    if s == 0:
                        continue
                    if tuples[1] != select[s]:
                        # print(tuples)
                        res.append(data_list[index])
        print(res)

    def atrributes_string(self, description) -> str:
        """Формируем из полей описания строку для запросов"""
        attributes = ""
        for index, i in enumerate(description):  # формируем строку атрибутов для запроса
            if index == 0:
                attributes += i
            else:
                attributes += ', ' + i
        return attributes

    def create_table(self, description, title):
        """Генерация запроса на создание БД."""
        request_create = "CREATE TABLE " + str(title) + " (id SERIAL  "
        for i in range(len(description)):
            if i != len(description):
                request_create += ", " + str(description[i]).lower() + " VARCHAR"
        request_create += " );"
        try:
            self.cur.execute(request_create)
            self.conn.commit()
        except Exception as er:
            print(er)

    def list_field(self, data_json) -> list:
        list_fields = [[]]  # список для полей
        tmp = 0
        for field in data_json:
            for key in field:
                list_fields[tmp].append(str(list(key.keys())[0]))
            list_fields.append([])
            tmp += 1
        for field in list_fields:
            for index, itm in enumerate(field):
                if itm in 'Наименование товара':
                    tmp = field[0]
                    field[0] = "Наименование товара"
                    field[index] = tmp
        for field in list_fields:
            for index, itm in enumerate(field):
                name = self.translator.translate(itm, src='ru')
                field[index] = name.text.lower().replace(" ", '_').replace(",", '')
        return list_fields

    def insert_table(self, data_json, title, description):
        """Генерация запроса встаки даннх в БД.
        title - название таблицы
        description - список ключей характеристик на английском"""
        inserts = []  # список для характеристик товара
        count = False
        list_fields = self.list_field(data_json)
        try:  # запрос на получение данных из таблицы
            request_select = "SELECT t.*, CTID FROM public.{} t LIMIT 501".format(title)
            self.cur.execute(request_select)
            request_select = self.cur.fetchall()
        except Exception as er:
            print(er)
        for i in data_json:
            if len(request_select) == 0:
                for x in i:
                    if 'Наименование товара' in x.keys():
                        name = x['Наименование товара'].split(' ')[0]
                        inserts[0].append(name)  # вставка первого элемента для запуска сиквенса
            for x in i:
                if 'Наименование товара' in x.keys():
                    name = x['Наименование товара'].split(' ')[0]
                    inserts.append([name])
        count = 0
        for i in data_json:
            if count < len(data_json):
                for x in i:
                    string = str(list(x.values())[0])
                    inserts[count].append(string)
            count += 1
        list_tuple = []  # спсиок кортежей
        for i in inserts:  # формируем кортеж из характеристик
            list_tuple.append(tuple(i))
        print("Список кортежей {}".format(list_tuple))

        try:  # вставка данных
            request_insert = "INSERT INTO " + str(title)
            for index, tuples in enumerate(list_tuple):
                if len(request_select) == 0:  # если БД пуста
                    for tmp in list_tuple:  # генерация зароса на вставку
                        attributes = self.atrributes_string(list_fields[index])
                        print("Attributes {}".attributes)
                        inserts = sql.SQL(request_insert + "{} VALUES {}".format(attributes, tmp))
                        self.cur.execute(inserts)
                        self.conn.commit()
                    break
                else:
                    attributes = self.atrributes_string(list_fields[index])
                    check_data = self.data_validation(request_select, tuples)  # проверка на совпадение данных
                    if check_data:
                        inserts = sql.SQL(request_insert + "{} VALUES {}".format(attributes, tuples))
                        self.cur.execute(inserts)
                        self.conn.commit()
        except Exception as er:
            print(er)

    def read_file_json(self, filename):
        with open(filename) as input_file:
            data = json.load(input_file)
            input_file.close()
            print(data)
        #self.traning_data(data_list=data)

    def traning_data(self, data_list):
        """Предворительная подготовка данных"""
        title = ''  # наименование вида товара на русском
        name = ''  # наименование вида товара на английском
        description = []  # список для ключей из характеристик о товаре
        description_max = []  # для максимальной длины харкатеристик, считаем как полную
        id = 0  # индекс максимальной харатеристики
        for itm in range(len(data_list)):  # подсчет длины каждой хакартеристики товара
            description_max.append(len(data_list[itm]))
        for index, itm in enumerate(description_max):  # находим индекс максимлаьной длины
            if itm == max(description_max):
                id = index
        for itm in data_list[id]:  # так как наименовае товара оказывается в конце после парсинга  характеристик
            if 'Наименование товара' in itm.keys():
                keys = str(list(itm.keys())[0])  # получение  ключа как строки
                title = itm['Наименование товара'].split(' ')[0]  # наименование вида товара на русском
                # print(title)
                result = self.translator.translate(keys, src='ru')  # перевод ключа на английский
                description.append(result.text.replace(" ", "_"))
                name = self.translator.translate(title, src='ru')
                name = name.text.lower()
                # print(result.text)
        for i in data_list[id]:  # работа с харектеристиакми товара
            if not 'Наименование товара' in i.keys():
                r = self.translator.translate(str(list(i.keys())[0]), src='ru')
                r = r.text.replace(",", "").replace(' ', "_").replace('(', "").replace(")", "")
                r = r.lower()
                description.append(r)
        check_create = self.cur.execute(
            "SELECT n.nspname, c.relname FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace "
            "WHERE c.relkind = 'r' AND n.nspname NOT IN('pg_catalog', 'citilink');")  # запрос для проверки создана ли
        # таблица
        list_table = self.cur.fetchall()  # спсисок существующих таблиц
        for itm in list_table:
            #
            if name in itm[1]:  # проверка существования таблицы
                self.insert_table(data_json=data_list,
                                  title=name,
                                  description=description)  # вставка данных если таблица существует
                break
            else:
                self.create_table(description=description,
                                  title='flash')


data_json = [{'Совместимость с брендом': 'Canon'},
             {'Ведущее число макс(ISO100)': '43 м'}, {'Зум, нижняя граница': '24 мм'},
             {'Зум, верхняя граница': '105 мм'}, {'FP-синхронизация': 'ДА'},
             {'Синхронизация по второй шторке': 'ДА'},
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
             {'url': 'https://www.citilink.ru/catalog/photo_and_video/photo_flashes/346629/'}], \
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
             {'url': 'https://www.citilink.ru/catalog/photo_and_video/photo_flashes/998318/'}]

"""if __name__ == '__main__':
    db = Database()
    db.traning_data(data_json)"""
