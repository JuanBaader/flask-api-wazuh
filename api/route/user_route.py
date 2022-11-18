from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.user_model import UserModel
from api.schema.user_schema import UserSchema
from api.service.user_service import UserService

user_api = Blueprint('users', __name__)
user_service = UserService()


@user_api.route('/')
@swag_from({
    'tags': ['users'],
    'definitions': {
        'multiple_users': {
            'type': 'object',
            'properties': {
                'total_items': {
                    '$ref': '#/definitions/total_items'
                },
                'data': {
                    'type': 'array',
                    'items': {
                        '$ref': '#/definitions/user_schema'
                    }
                }
            }
        },
        'user_schema': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer'
                },
                'name': {
                    'type': 'string'
                },
                'username': {
                    'type': 'string'
                },
                'email': {
                    'type': 'string'
                },
                'phone': {
                    'type': 'string'
                },
                'website': {
                    'type': 'string'
                },
                'company': {
                    '$ref': '#/definitions/company'
                },
                'address': {
                    '$ref': '#/definitions/address'
                },
            }
        },
        'total_items': {
            'type': 'integer'
        },
        'company': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string'
                },
                'catchPhrase': {
                    'type': 'string'
                },
                'bs': {
                    'type': 'string'
                }
            }
        },
        'address': {
            'type': 'object',
            'properties': {
                'street': {
                    'type': 'string'
                },
                'suite': {
                    'type': 'string'
                },
                'city': {
                    'type': 'string'
                },
                'zipcode': {
                    'type': 'string'
                },
                'geo': {
                    '$ref': '#/definitions/geo'
                }
            }
        },
        'geo': {
            'type': 'object',
            'properties': {
                'lat': {
                    'type': 'string'
                },
                'long': {
                    'type': 'string'
                }
            }
        }
    },
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'List of users',
            'schema': {
                '$ref': '#/definitions/multiple_users'
            }
        }
    }
})
def users():
    """
    Returns all users
    Method that returns a list of all users
    ---
    """

    return user_service.get_users()


@user_api.route('/<uid>')
@swag_from({
    'tags': ['users'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': {
                '$ref': '#/definitions/user_schema'
            },
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'No user found with with specified id',
        }
    }
})
def user_by_id(uid):
    """
    Returns one user
    Method that returns one users by its id
    ---
    """
    return user_service.get_users_by_id(uid)


@user_api.route('/<uid>/tasks')
@swag_from({
    'tags': ['users', 'tasks'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': {
                '$ref': '#/definitions/multiple_tasks'
            }
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'No user found with with specified id',
        }
    }
})
def user_tasks(uid):
    """
    Returns one user's tasks
    Method that returns a list task owned by a user by its id
    ---
    """
    return user_service.get_tasks_of_user(uid)


@user_api.route('/<uid>/tasks/<tid>')
@swag_from({
    'tags': ['users', 'tasks'],
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': {
                '$ref': '#/definitions/task_schema'
            }
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'No user or task found with with specified id',
        }
    }
})
def user_task_by_id(uid, tid):
    """
    Returns one user's task
    Method that returns one task given a user id and a task id
    ---
    """
    return user_service.get_task_by_id_of_user(uid, tid)
