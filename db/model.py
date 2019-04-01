from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    task = db.Column(db.String(60))


class TaskSchema(ma.ModelSchema):

    class Meta:
        model = Task
