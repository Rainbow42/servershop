import pika
import json



def read_file(filename):
    with open('url_list.json') as input_file:
        data = json.load(input_file)
        input_file.close()
    return data


class Send:

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='direct_logs',
                                 exchange_type='fanout')
        messages = self.message('url_list.json')
        for i in messages:
            channel.basic_publish(exchange='direct_logs',
                                  routing_key='',
                                  body=i,
                                  properties=pika.BasicProperties(
                                      delivery_mode=2,
                                  ))
        print(" [x] Sent %r" % messages)
        connection.close()

    def message(self, json_file) -> list:
        data_list = (read_file(json_file))
        url_list = []
        for i in data_list:
            url_list.append(i['url'])
        return url_list


