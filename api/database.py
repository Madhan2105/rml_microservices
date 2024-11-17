import os
from dotenv import load_dotenv

from models import db

load_dotenv()


class DatabaseConnection:
    def __init__(self, flask_app):
        """Initialize Object."""
        self.app = flask_app
        self.host = os.getenv("POSTGRES_HOST")
        self.dbname = os.getenv("POSTGRES_DB")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establish a connection with database."""
        path = (
            'postgresql://{}:{}@{}:5432/{}'
        ).format(
            self.user, self.password, self.host, self.dbname
        )
        self.app.config['SQLALCHEMY_DATABASE_URI'] = path
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.app)

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
