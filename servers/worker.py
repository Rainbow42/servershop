import pika
import requests
from config import FILE_HTML_SPECIFICATIONS, FILE_NAME_JSON_SPECIFICATIONS, HEADERS
from parse.parse_specifications import Parse
from parse.url import Date
import time
from work_file import json_file


def callback(body):
    """Отправка на парсинг url с полным описанием тоавара"""
    body = body.decode('utf-8')
    print(body)
    s = requests.Session()
    result = []
    url = Date()
    html, status_code = url.get(filename=FILE_HTML_SPECIFICATIONS,
                                url=body,
                                session=s,
                                headers=HEADERS,)
    print(" [x] Answer {} Received {} ".format(status_code, body))
    if status_code == 200:
        date = Parse()
        result.append(date.search(text=html,
                                  filename=FILE_NAME_JSON_SPECIFICATIONS,
                                  url=body))

        print(result)
        print(" [x] Done")



def Worker():
    """Подписчик"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue', durable=True)

    #channel.exchange_declare(exchange='direct_logs',
                            # exchange_type='fanout')

    result = channel.queue_declare(queue='queue', exclusive=False)  # очередь
    queue_name = result.method.queue

    print('\n [*] Waiting for messages. To exit press CTRL+C')
    method_frame, _, body = channel.basic_get('queue')
    while True:  # пока есь данные в очереди
        try:
            if body:
                callback(body)
                channel.basic_ack(method_frame.delivery_tag)
                # time.sleep(2)
            method_frame, _, body = channel.basic_get('queue')
        except Exception as err:
            return str(err)
