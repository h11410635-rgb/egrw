from flask import Flask

from . import db, routes
from .config import SECRET_KEY


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    db.init_db()
    routes.register(app)
    return app
