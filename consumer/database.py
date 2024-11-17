import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConnection:
    def __init__(self):
        """Initialize Object."""
        self.host = os.getenv("POSTGRES_HOST")
        self.dbname = os.getenv("POSTGRES_DB")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        self.connection = psycopg2.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create_table_if_not_exists(self):
        """Automatically create the tasks table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            description TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Table 'tasks' is ready.")

    def insert_task(self, description):
        """Insert a task into the database."""
        insert_query = sql.SQL("""
            INSERT INTO tasks (description)
            VALUES (%s)
        """)
        self.cursor.execute(insert_query, (description,))
        self.connection.commit()