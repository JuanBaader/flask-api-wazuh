from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from api.model.task_model import TaskModel
from api.schema.task_schema import TaskSchema
from api.service.task_service import TaskService

task_api = Blueprint('tasks', __name__)
taskService = TaskService()


@task_api.route('/', methods=['GET'])
@swag_from({
    "parameters": [
        {
            "name": "completed",
            "in": "path",
            "type": "bool",
            "required": False
        },
        {
            "name": "title",
            "in": "path",
            "type": "string",
            "required": False
        }
    ],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': TaskSchema
        }
    }
})
def tasks():
    '''
    Returns all Tasks
    Method that returns a list of all Tasks
    ---
    '''
    args = request.args
    # if args.has_key("completed"):
    #     completed = args.completed
    # else:
    #     completed = None
    return taskService.get_tasks(args.get('completed'), args.get('title')), 200


@task_api.route('/<tid>', methods=['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': TaskSchema
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'No task with specified id'
        }
    }
})
def task_by_id(tid):
    '''
    Returns one task
    Method that returns a list a task specified by its id
    ---
    '''
    return taskService.get_task_by_id(int(tid)), 200
