import rabbitpy

url = 'amqp://u:p@url:5672/%2F'

connection = rabbitpy.Connection(url)
channel = connection.channel()
exchange = rabbitpy.Exchange(channel, 'exchage.01')
exchange.declare()

queue = rabbitpy.Queue(channel, 'queue.01')
queue.declare()
queue.bind(exchange, 'example-routing-key')
channel.enable_publisher_confirms()

message = rabbitpy.Message(channel,
                               'Test message',
                               {'content_type': 'text/plain'},
                               opinionated=True)

if message.publish(exchange, 'example-routing-key'):
    print('message OK')

connection.close()