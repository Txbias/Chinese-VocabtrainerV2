from flask import Blueprint, render_template, request
import urllib.parse

from database import user

login_blueprint = Blueprint('root_blueprint', __name__, template_folder='templates')


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = urllib.parse.unquote(request.data.decode('utf-8')).split('&')
        data = [d.split('=')[1] for d in data]

        username = data[0]
        password = data[1]

        if user.valid_login(username, password):
            return 'true'
        else:
            return 'false'
