from app.domain.usecases.auth import AuthenticationUseCase

from app.application.models.user import AuthInputModel
from app.application.protocols.cryptography.encrypter import Encrypter

from app.presentation.protocols.controller import Controller
from app.presentation.protocols.http import HttpResponse, HttpRequest


class AuthenticationController(Controller):
    def __init__(self, use_case: AuthenticationUseCase, encrypter: Encrypter):
        self._use_case = use_case
        self._encrypter = encrypter

    def handle(self, req: HttpRequest) -> HttpResponse:
        try:
            data = AuthInputModel(**req.data)
            is_authenticated = self._use_case.authenticate(data.email, data.password)
            if is_authenticated:
                token = {
                    'access_token': self._encrypter.encrypt(data.email)
                    # 'refresh_token': self._token.create_refresh(user.email)
                }
                return token, 200
        except ValueError as e:
            return {'error': e.args[0]}, 401
        except TypeError as e:
            return {'error': e.args[0]}, 400
