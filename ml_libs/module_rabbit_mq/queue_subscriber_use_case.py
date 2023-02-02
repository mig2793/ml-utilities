from .connection_rabbit_mq import ConectionRabbitMQ


class Subscriber:
    channel = None
    connection = None

    def __init__(self, queueName, bindingKey, config):
        self.connection = ConectionRabbitMQ().connection
        self.channel = self.connection.channel()
        self.config = config
        self.queueName = queueName
        self.bindingKey = bindingKey

    def __del__(self):
        self.connection.close()
        
    def setup(self):
        self.channel.exchange_declare(
            exchange=self.config["exchange"],
            exchange_type="topic",
            durable=True,
        )
        self.channel.queue_declare(queue=self.queueName)
        self.channel.queue_bind(
            queue=self.queueName,
            exchange=self.config["exchange"],
            routing_key=self.bindingKey,
        )
