import pika
import time
from service import FileReaderService
from connection import RabbitMQPublisher

path = "data.txt"
publisher = RabbitMQPublisher(
    queue_name='task_queue'
)
fs = FileReaderService(
    path,
    publisher
)
fs.process_file()
