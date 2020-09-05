import pika
from config import FILE_NAME_JSON
from work_file import read_file_json
import time


def message(json_file) -> list:
    data_list = read_file_json(json_file)
    url_list = []
    for i in data_list:
        url_list.append(i['url'])
    return url_list


class Send:
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        """channel.exchange_declare(exchange='direct_logs',
                                 exchange_type='fanout')"""  # cоздание очереди
        channel.queue_declare(queue='my_queue')

        messages = message(FILE_NAME_JSON)
        print(messages)
        for i in messages:
            channel.basic_publish(exchange='',
                                  routing_key='my_queue',
                                  body=i,
                                  properties=pika.BasicProperties(
                                      delivery_mode=2,
                                  ))
            time.sleep(1)

        connection.close()
