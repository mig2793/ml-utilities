from .connection_rabbit_mq import ConectionRabbitMQ


class QueuePublishCase:
    channel = None

    def __init__(self, config):
        connection = ConectionRabbitMQ().connection
        self.channel = connection.channel()
        self.config = config

    def publish(self, routingKeyName, message, queueName):
        self.channel.exchange_declare(
            self.config["exchange"], durable=True, exchange_type="topic"
        )
        self.channel.queue_declare(queue=queueName)
        self.channel.queue_bind(
            exchange=self.config["exchange"],
            queue=queueName,
            routing_key=routingKeyName,
        )
        self.channel.basic_publish(
            exchange=self.config["exchange"], routing_key=routingKeyName, body=message
        )
        print(" [x] Sent message %r for %r" % (message, routingKeyName))
