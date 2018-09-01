import rabbitpy

url = 'amqp://u:p@url:5672/%2F'

connection = rabbitpy.Connection(url)

channel = connection.channel()

exchange = rabbitpy.Exchange(channel, 'exchage.01')

exchange.declare()

queue = rabbitpy.Queue(channel, 'queue.01')
queue.declare()
queue.bind(exchange, 'example-routing-key')

tx = rabbitpy.Tx(channel)
tx.select()

message = rabbitpy.Message(channel,
                               'Test message',
                               {'content_type': 'text/plain',
                               'delivery_mode': 2,
                               'message_type': 'important'})

message.publish(exchange, 
                'example-routing-key')


try:
    if tx.commit():
        print('Transaction OK')
except rabbitpy.exceptions.NoActiveTransactionError:
    print('error')

connection.close()