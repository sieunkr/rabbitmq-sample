import pika
import sys

credentials = pika.PlainCredentials('u', 'p')
parameters =  pika.ConnectionParameters('url', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()\

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue='queue.01',
                      no_ack=True)

channel.start_consuming()
