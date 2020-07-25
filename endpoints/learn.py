from flask import Blueprint, render_template
from database import vocab

learn_blueprint = Blueprint('root', __name__, template_folder='templates')


@learn_blueprint.route('/learn')
def site_root():
    vocabs = vocab.get_all()
    return render_template('learn.html', data=vocabs)
