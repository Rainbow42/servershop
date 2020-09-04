import sys

sys.path.append('../')
import pika
from config import FILE_NAME_JSON
from work_file import read_file_json


class Send:

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='direct_logs',
                                 exchange_type='fanout')
        messages = self.message(FILE_NAME_JSON)
        for i in messages:
            channel.basic_publish(exchange='direct_logs',
                              routing_key='',
                              body=i,
                              properties=pika.BasicProperties(
                              delivery_mode=2,
                              ))

        # print(" [x] Sent %r" % messages)
        connection.close()

    def message(self, json_file) -> list:
        data_list = read_file_json(json_file)
        url_list = []
        for i in data_list:
            url_list.append(i['url'])
        return url_list
