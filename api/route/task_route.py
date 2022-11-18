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
    "definitions": {
        "to_return": {
            "type": "object",
            "properties": {
                "total_items": {
                    "$ref": "#/definitions/total_items"
                },
                "data": {
                    "type": "array",
                    "items": {
                        '$ref': "#/definitions/schema"
                    }
                }
            }
        },
        "schema": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "user_id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "completed": {
                    "type": "boolean"
                }
            }
        },
        "total_items": {
            "type": "integer"
        }
    },
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'A list of task that match the parameters',
            'schema': {
                "$ref": "#/definitions/to_return"
            }
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
    return taskService.get_task_by_id(int(tid))
