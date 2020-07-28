from flask import Flask
from database.database_manager import init_db
from endpoints.add_vocab import add_vocab_blueprint
from endpoints.learn import learn_blueprint
from endpoints.login import login_blueprint
from endpoints.register import register_blueprint
from endpoints.root import root_blueprint
import settings


def configure_app(flask_app: Flask) -> None:
    flask_app.debug = settings.FLASK_DEBUG
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME


def init_app() -> Flask:
    flask_app = create_app()
    init_db()
    return flask_app


def create_app() -> Flask:
    flask_app = Flask(__name__)
    configure_app(flask_app)
    flask_app.register_blueprint(add_vocab_blueprint)
    flask_app.register_blueprint(learn_blueprint)
    flask_app.register_blueprint(login_blueprint)
    flask_app.register_blueprint(register_blueprint)
    flask_app.register_blueprint(root_blueprint)
    return flask_app


if __name__ == '__main__':
    app = init_app()
    app.run()
