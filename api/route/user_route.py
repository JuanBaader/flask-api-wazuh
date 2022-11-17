from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.welcome import WelcomeModel
from api.schema.welcome import WelcomeSchema
from api.service.user_service import UserService

user_api = Blueprint('users', __name__)


@user_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit',
            'schema': WelcomeSchema
        }
    }
})
def users():
    """
    Returns all users
    Method that returns a list of all users
    ---
    """
    user_service = UserService()
    return user_service.getUserById(1), 200
