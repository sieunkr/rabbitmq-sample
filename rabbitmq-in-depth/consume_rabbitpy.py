import rabbitpy

url = 'amqp://u:p@url:5672/%2F'

connection = rabbitpy.Connection(url)

connection = rabbitpy.Connection(url)

channel = connection.channel()

queue = rabbitpy.Queue(channel, 'queue.01')

while len(queue) > 0:
    message = queue.get()
    print('Message:')
    print(' ID: %s' % message.properties['message_id'])
    print(' Body: %s' % message.body)
    message.ack()


