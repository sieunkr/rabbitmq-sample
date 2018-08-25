import pika

credentials = pika.PlainCredentials('u', 'p')
parameters =  pika.ConnectionParameters('url', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(exchange="exchage.01", exchange_type="direct")

channel.basic_publish(exchange='exchage.01',
                      routing_key='example-routing-key',
                      body='test by pika')


connection.close()