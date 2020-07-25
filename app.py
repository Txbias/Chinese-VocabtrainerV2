from flask import Flask
from database.database_manager import init_db
from endpoints.add_vocab import add_vocab_blueprint
from endpoints.learn import learn_blueprint
from endpoints.login import login_blueprint
from endpoints.register import register_blueprint
import settings

app = Flask(__name__)


def configure_app(flask_app: Flask) -> None:
    flask_app.debug = settings.FLASK_DEBUG
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME


def init_app(flask_app: Flask) -> None:
    configure_app(flask_app)
    flask_app.register_blueprint(add_vocab_blueprint)
    flask_app.register_blueprint(learn_blueprint)
    flask_app.register_blueprint(login_blueprint)
    flask_app.register_blueprint(register_blueprint)
    init_db()


def main() -> None:
    init_app(app)
    app.run()


if __name__ == '__main__':
    main()
