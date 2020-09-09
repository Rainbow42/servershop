import pika
import requests
import sys
from threading import Thread
from multiprocessing import Process
from config import FILE_HTML_SPECIFICATIONS, FILE_NAME_JSON_SPECIFICATIONS, HEADERS, COUNT_THREAD
from parse.parse_specifications import Parse
from parse.url import Date
import time
from work_file import json_file


def callback(ch, method, properties, body):
    """Отправка на парсинг url с полным описанием тоавара"""
    body = body.decode('utf-8')
    print(body)
    s = requests.Session()
    result = []
    url = Date()
    html, status_code = url.get(filename=FILE_HTML_SPECIFICATIONS,
                                url=body,
                                session=s,
                                headers=HEADERS, )
    print(" [x] Answer {} Received {} ".format(status_code, body))
    if status_code == 200:
        date = Parse()
        result.append(date.search(text=html,
                                  filename=FILE_NAME_JSON_SPECIFICATIONS,
                                  url=body))

        # print(result)
        print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def Worker():
    """Подписчик"""
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                                   5672,
                                                                   '/',
                                                                   credentials))
    channel = connection.channel()

    result = channel.queue_declare(queue='queue', durable=True)  # очередь
    queue_name = result.method.queue

    print('\n [*] Waiting for messages. To exit press CTRL+C')
    try:
        for count_thread in range(COUNT_THREAD):
            t1 = Thread(target=channel.basic_consume, args=(callback, 'queue',))
            #  t1 = Process(target=channel.basic_consume, args=(callback, 'queue',))
            t1.start()
            time.sleep(2)
        channel.start_consuming()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    Worker()
