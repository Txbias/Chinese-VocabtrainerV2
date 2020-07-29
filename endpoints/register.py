from flask import Blueprint, render_template, request
from database import user
from database.user import User
import urllib.parse
import json
from utils import Response

register_blueprint = Blueprint('register_blueprint', __name__, template_folder='templates')


@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        data = urllib.parse.unquote(request.data.decode('utf-8')).split('&')
        data = [d.split('=')[1] for d in data]

        username = data[0]
        password = data[1]
        password_repeat = data[2]

        # TODO: handle errors
        if len(username) == 0:
            response = Response(False, 'The username can\'t be empty')
            return json.dumps(response.__dict__)

        if password != password_repeat:
            response = Response(False, 'Both passwords must be the same')
            return json.dumps(response.__dict__)

        if len(password) == 0:
            response = Response(False, 'The password can\'t be empty')
            return json.dumps(response.__dict__)

        if user.exists(username):
            response = Response(False, 'The entered username is already taken')
            return json.dumps(response.__dict__)
        else:
            # Username is unique
            # The account gets added to the database
            u = User()

            pw_hash, salt = user.hash_password(password)

            u.username = username
            u.password_hash = pw_hash
            u.salt = salt
            user.add(u)

            response = Response(True)
            return json.dumps(response.__dict__)
