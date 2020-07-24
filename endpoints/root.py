from flask import Blueprint, render_template
from database import vocab

root_blueprint = Blueprint('root', __name__, template_folder='templates')


@root_blueprint.route('/')
def site_root():
    vocabs = vocab.get_all()
    return render_template('learn.html', data=vocabs)
