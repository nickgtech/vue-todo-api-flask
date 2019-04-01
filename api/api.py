from flask import Flask
from flask_restful import Api
from db.model import db, ma
from api_classes import TaskResource
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
api = Api(app)
db.init_app(app)
ma.init_app(app)

CORS(app)

api.add_resource(TaskResource,
                 '/api/task',
                 '/api/task/<id>')

if __name__ == '__main__':
    app.run(debug=True)
