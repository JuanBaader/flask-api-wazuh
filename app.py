from flask import Flask
from flasgger import Swagger
from api.route.user_route import user_api
from api.route.task_route import task_api

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'User and tasks API for Wazuh',
    }
    swagger = Swagger(app)
     ## Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(user_api, url_prefix='/api/users')
    app.register_blueprint(task_api, url_prefix='/api/tasks')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
