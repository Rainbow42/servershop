import sys

sys.path.append('../')
import pika
import requests
from config import FILE_HTML_SPECIFICATIONS, FILE_NAME_JSON_SPECIFICATIONS
from service_parse_specifications.parse import Parse
from parse.url import Date
from work_file import read_file


def callback(ch, method, properties, body):
    s = requests.Session()
    url = Date()
    html = url.get(filename=FILE_HTML_SPECIFICATIONS,
                   url=body,
                   session=s)

    date = Parse()
    technical_list = date.search(text=read_file(FILE_HTML_SPECIFICATIONS),
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

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='direct_logs',
                           queue=queue_name)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.basic_consume(queue=queue_name,
                              on_message_callback=callback,
                              # exchange='direct_logs',
                              auto_ack=True)

        channel.start_consuming()


Worker()
