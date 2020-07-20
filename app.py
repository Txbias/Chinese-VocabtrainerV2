from flask import Flask, render_template
from database.database_manager import init_db
from database import vocab
import settings

app = Flask(__name__)


def configure_app(flask_app: Flask) -> None:
    flask_app.debug = settings.FLASK_DEBUG
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME


def init_app(flask_app: Flask) -> None:
    configure_app(flask_app)
    init_db()


def main() -> None:
    init_app(app)
    app.run()


@app.route("/")
def learn_route():
    vocabs = vocab.get_all()
    return render_template('learn.html', data=vocabs)


if __name__ == "__main__":
    main()
