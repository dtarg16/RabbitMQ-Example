import os
import pika
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('CLOUDAMQP_URL')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel

channel.exchange_declare('test_exchange')  # declare exchange
channel.queue_declare(queue='test_queue')  # declare queue
channel.queue_bind('test_queue', 'test_exchange', 'tests')  # create binding between queue and exchange

# publish message
channel.basic_publish(
    body='Hello RabbitMQ!',
    exchange='test_exchange',
    routing_key='tests'
)

print(' Message sent.')
channel.close()
connection.close()
