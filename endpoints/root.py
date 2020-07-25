from flask import Blueprint, redirect, url_for

root_blueprint = Blueprint('root_blueprint', __name__, template_folder='templates')


@root_blueprint.route('/')
def root():
    # TODO: Look for session cookies
    return redirect(url_for('/login'))
