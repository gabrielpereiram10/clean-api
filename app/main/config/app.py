from flask import Flask

from app.main.routers.authentication import auth


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth)

    return app
