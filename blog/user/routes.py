import os

from flask import Blueprint, render_template

from blog.user.forms import RegistrationForm, LoginForm
from blog import bcrypt, db
from blog.models import User


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.passwod.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', user.username)

        if not os.path.exists(full_path):
            os.mkdir(full_path)