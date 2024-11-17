# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tasks(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"<Task {self.name}>"
