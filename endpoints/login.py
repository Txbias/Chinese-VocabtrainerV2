from flask import Blueprint, render_template, request
import urllib.parse
import json

from database import user
from utils import Response

login_blueprint = Blueprint('login_blueprint', __name__, template_folder='templates')


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = urllib.parse.unquote(request.data.decode('utf-8')).split('&')
        data = [d.split('=')[1] for d in data]

        username = data[0]
        password = data[1]

        if len(username) == 0 or len(password) == 0:
            response = Response(False, 'The username and the password can\'t be empty')
            return json.dumps(response.__dict__)

        if user.valid_login(username, password):
            response = Response(True)
            return json.dumps(response.__dict__)
        else:
            response = Response(False, 'Wrong password')
            return json.dumps(response.__dict__)
