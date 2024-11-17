import pika
from dotenv import load_dotenv
import os


class RabbitMQPublisher:
    """Handles publishing messages to a RabbitMQ queue."""
    def __init__(
            self, queue_name, host='localhost', username='guest',
            password='guest'
    ):
        """Initialize Object."""
        self.queue_name = queue_name
        self.host = os.getenv("RABBITMQ_HOST")
        self.user = os.getenv("RABBITMQ_USER")
        self.password = os.getenv("RABBITMQ_PASSWORD")
        self.connection = None
        self.channel = None
        self._connect()

    def _connect(self):
        """Connect with Rabbit MQ Service."""
        credentials = pika.PlainCredentials(self.user, self.password)
        connection_params = pika.ConnectionParameters(
            host=self.host, credentials=credentials
        )
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def publish(self, message):
        """Publish the task."""
        self.channel.basic_publish(
            exchange='', routing_key=self.queue_name, body=message
        )

    def close(self):
        """Close the Open Connection."""
        if self.connection and self.connection.is_open:
            self.connection.close()
