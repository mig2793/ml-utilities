import json
import traceback
import pika
import os


class ConectionRabbitMQ(object):
    """
    Singleton class for establishing a connection to a RabbitMQ server.
    The connection is established using the user, password, and URL specified in environment variables.
    If the connection fails, an error is logged and the program is terminated.
    """

    connection = None
    user: str = ""
    password: str = ""
    url: str = ""

    def __new__(cls):
        """
        Implement the singleton pattern by only allowing a single instance of the class to be created.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(ConectionRabbitMQ, cls).__new__(cls)
        return cls.instance

    def __init__(self, user="", password="", url=""):
        self.user = user == "" and os.getenv("RABBIT_MQ_USER") or user
        self.password = password == "" and os.getenv("RABBIT_MQ_PASSWORD") or password
        self.url = url == "" and os.getenv("RABBIT_MQ_URL") or url

        try:
            credentials = pika.PlainCredentials(self.user, self.password)
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.url, credentials=credentials)
            )
        except:
            error = json.dumps(vars(error))
