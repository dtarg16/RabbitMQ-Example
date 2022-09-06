# RabbitMQ-Example


## Setup

- Create .env file and paste this line, change the link to your own

```CLOUDAMQP_URL=amqps://user:password@host/user```

- Run command from below to run publisher and send the message

```python publisher.py```

- Run command from below to run consumer and receive the message

```python3 consumer.py```