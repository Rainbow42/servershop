import pika
import time


def message(list_date) -> list:
    """Получение url товаров из списка"""
    url_list = []
    for itm in list_date:
        for tmp in itm:
            url_list.append(tmp['url'])
    return url_list


def Send(messages):
    """Создание очереди из списка  url"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')  # наименование очереди
    messages = message(messages)
    for i in messages:  # отправка url
        channel.basic_publish(exchange='',
                              routing_key='my_queue',
                              body=i,
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))
        time.sleep(1)

    connection.close()
