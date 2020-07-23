from flask import Flask, render_template, request
from database.database_manager import init_db
from database import vocab
from database.vocab import Vocabulary
import settings
import urllib.parse

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


@app.route('/')
def learn_route():
    vocabs = vocab.get_all()
    return render_template('learn.html', data=vocabs)


@app.route('/addVocab', methods=['POST'])
def add_vocab():
    if request.method != 'POST':
        return ''

    data = urllib.parse.unquote(request.data.decode('utf-8')).split('&')
    data = [d.split('=')[1] for d in data]

    voc = Vocabulary()
    voc.pinyin = data[0]
    voc.german = data[1]
    voc.character = data[2]
    vocab.add(voc)

    return ''


if __name__ == '__main__':
    main()
