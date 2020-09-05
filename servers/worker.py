import pika
import requests
from config import FILE_HTML_SPECIFICATIONS, FILE_NAME_JSON_SPECIFICATIONS
from service_parse_specifications.parse import Parse
from parse.url import Date
from work_file import read_file


def callback(body):
    s = requests.Session()
    url = Date()
    html = url.get(filename=FILE_HTML_SPECIFICATIONS,
                   url=body,
                   session=s)

    date = Parse()
    date.search(text=html,
                filename=FILE_NAME_JSON_SPECIFICATIONS)
    print(html)
    print(" [x] Received {}".format(body))
    print(" [x] Done")


class Worker:
     def __init__(self):
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
        try:
            while body:
                try:
                    if body:
                        callback(body)
                        channel.basic_ack(method_frame.delivery_tag)
                    else:
                        return "No url'"
                except:
                    continue
        except:
            print('Error messages')
