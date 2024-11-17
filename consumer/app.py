from connection import RabbitMQConnection
from service import Consumer
from database import DatabaseConnection

rbq = RabbitMQConnection(
    queue_name='task_queue'
)
db = DatabaseConnection()
Consumer(
    rbq,
    db

).start_consuming()
