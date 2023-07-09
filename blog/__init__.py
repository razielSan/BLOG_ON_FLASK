from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask


db = SQLAlchemy()
bcypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    bcypt.init_app(app)

    from blog.main.routes import main
    from blog.user.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app