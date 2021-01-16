from flask import Blueprint, request

from app.main.factories.authentication import create_authentication_controller
from app.main.adapters.flask_router import flask_router_adapter

auth = Blueprint('auth', __name__)


@auth.route('/auth', methods=['POST'])
def login():
    router = flask_router_adapter(create_authentication_controller())
    return router(request)
