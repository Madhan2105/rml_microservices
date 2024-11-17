import pika
from dotenv import load_dotenv
import os

load_dotenv()


class RabbitMQConnection:
    def __init__(self, queue_name='task_queue'):
        """Initialize Object."""
        self.host = os.getenv("RABBITMQ_HOST")
        self.user = os.getenv("RABBITMQ_USER")
        self.password = os.getenv("RABBITMQ_PASSWORD")
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

    def _connect(self):
        """Establish a connection to RabbitMQ and create a channel."""
        credentials = pika.PlainCredentials(self.user, self.password)
        connection_params = pika.ConnectionParameters(
            host=self.host, credentials=credentials
        )
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def close(self):
        """Close the connection."""
        if self.connection and self.connection.is_open:
            self.connection.close()

    def get_channel(self):
        """Return the channel if it's already connected."""
        return self.channel
