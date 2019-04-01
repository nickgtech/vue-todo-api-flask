from flask import request, jsonify
from flask_restful import Resource
from db.model import Task, TaskSchema,db


class TaskResource(Resource):

    def get(self, id=None):
        if id == None:
            tasks = Task.query.all()
            taskSchema = TaskSchema(many=True)
            output = taskSchema.dump(tasks).data
            return output
        else:
            task = Task.query.filter_by(id=id).first()
            taskSchema = TaskSchema()
            output = taskSchema.dump(task).data
            return output

    def post(self):
        data = request.get_json(force=True)
        task = Task(task=data['task'])
        db.session.add(task)
        db.session.commit()
        return 'task'

    def delete(self, id):
        task = Task.query.filter_by(id=id).first()
        taskSchema = TaskSchema()
        db.session.delete(task)
        db.session.commit()
        return 'it\'s gone yo'
