import pika
import requests
from config import FILE_HTML_SPECIFICATIONS, FILE_NAME_JSON_SPECIFICATIONS, HEADERS
from parse.parse_specifications import Parse
from parse.url import Date
import time
from multiprocessing import Process


def callback(body):
    """Отправка на парсинг url с полным описанием тоавара"""
    s = requests.Session()
    url = Date()
    html, status_code = url.get(filename=FILE_HTML_SPECIFICATIONS,
                                url=body,
                                session=s,
                                headers=HEADERS)
    print(" [x] Answer {} Received {} ".format(status_code, body))
    if status_code == 200:
        date = Parse()
        result = date.search(text=html,
                             filename=FILE_NAME_JSON_SPECIFICATIONS)
        # print(result)
        print(" [x] Done")


def Worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs',
                             exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)  # очередь
    queue_name = result.method.queue

    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name)

    print('\n [*] Waiting for messages. To exit press CTRL+C')
    method_frame, _, body = channel.basic_get('my_queue')
    while method_frame:  # пока есь данные в очереди
        try:
            if body:
                callback(body)
                channel.basic_ack(method_frame.delivery_tag)
                time.sleep(2)
                method_frame, _, body = channel.basic_get('my_queue')
            else:
                channel.close()
                return "No url'"
        except Exception as err:
            return str(err)



