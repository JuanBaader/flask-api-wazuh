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
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'List of users',
            'schema': UserSchema
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
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': UserSchema
        }
    }
})
def user_by_id(uid):
    """
    Returns all users
    Method that returns a list of all users
    ---
    """
    return user_service.get_users_by_id(uid)


@user_api.route('/<uid>/tasks')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': UserSchema
        }
    }
})
def user_tasks(uid):
    """
    Returns all users
    Method that returns a list of all users
    ---
    """
    user_service = UserService()
    return user_service.get_task_by_id_of_user(uid)


@user_api.route('/<uid>/tasks/<tid>')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': UserSchema
        }
    }
})
def user_task_by_id(uid, tid):
    """
    Returns all users
    Method that returns a list of all users
    ---
    """
    return user_service.get_task_by_id_of_user(uid, tid)
