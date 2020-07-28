from flask import Blueprint, render_template, request
from database import user
from database.user import User
import urllib.parse

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

        if user.exists(username):
            return "false"
        else:
            # Username is unique
            # The account gets added to the database
            u = User()

            pw_hash, salt = user.hash_password(password)

            u.username = username
            u.password_hash = pw_hash
            u.salt = salt
            user.add(u)

            return "true"
