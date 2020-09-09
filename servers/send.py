import pika
import time


def message(list_date) -> list:
    """Получение url товаров из списка"""
    # print(list_date)
    url_list = []
    for itm in list_date:
        for tmp in itm:
            url_list.append(tmp['url'])
    return url_list


def Send(messages):
    """Поставщик. Создание очереди из списка  url"""
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                                   5672,
                                                                   '/',
                                                                   credentials))
    channel = connection.channel()
    channel.queue_declare(queue='queue',durable=True) # наименование очереди
    messages = message(messages)
    for m in messages:  # отправка url
        # print(m)
        channel.basic_publish(exchange='',
                              routing_key='queue',
                              body=m,
                              properties=pika.BasicProperties(
                                  delivery_mode=2))
        time.sleep(1)

    connection.close()
