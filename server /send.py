import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='fanout')
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))
print(" [x] Sent %r" % message)
connection.close()
