from flask import Blueprint, request
import urllib.parse

from database import vocab
from database.vocab import Vocabulary


add_vocab_blueprint = Blueprint('add_vocab', __name__, template_folder='templates')


@add_vocab_blueprint.route('/addVocab', methods=['POST'])
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
