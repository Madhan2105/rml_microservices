import json


class Consumer:
    def __init__(self, rabbitmq, database):
        """Initialize Object."""
        self.rabbitmq = rabbitmq
        self.database = database
        self.database.create_table_if_not_exists()

    def callback(self, ch, method, properties, body):
        """This function will process the task/message."""
        print(f"Received message: {body.decode()}")
        body = body.decode()
        self.process_task(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def process_task(self, task):
        """Simulate processing the task."""
        print(f"Processing task: {task}")
        self.database.insert_task(task)

    def start_consuming(self):
        """Start consuming messages from the queue."""
        # Connect to RabbitMQ
        self.rabbitmq._connect()

        print(
            f"Waiting for messages in {self.rabbitmq.queue_name}"
            ". To exit press CTRL+C"
        )
        self.rabbitmq.get_channel().basic_consume(
            queue=self.rabbitmq.queue_name, on_message_callback=self.callback
        )

        # Start consuming messages
        self.rabbitmq.get_channel().start_consuming()

    def stop_consuming(self):
        """Stop the consumer and close the connection."""
        self.rabbitmq.close()
        print("Stopped consuming.")


if __name__ == "__main__":
    # Use RabbitMQ container name if running with Docker
    consumer = Consumer(host='rabbitmq')
    consumer.start_consuming()
