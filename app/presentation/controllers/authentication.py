from app.domain.usecases.auth import AuthenticationUseCase

from app.application.models.user import AuthInputModel

from app.presentation.protocols.controller import Controller
from app.presentation.protocols.token_generator import TokenGenerator
from app.presentation.protocols.http import HttpResponse, HttpRequest


class AuthenticationController(Controller):
    def __init__(self, use_case: AuthenticationUseCase, token: TokenGenerator):
        self._use_case = use_case
        self._token = token

    def handle(self, req: HttpRequest) -> HttpResponse:
        try:
            data = AuthInputModel(**req.data)
            is_authenticated = self._use_case.authenticate(data.email, data.password)
            if is_authenticated:
                token = {
                    'access_token': self._token.generate(data.email)
                    # 'refresh_token': self._token.create_refresh(user.email)
                }
                return token, 200
        except ValueError as e:
            return {'error': e.args[0]}, 401
        except TypeError as e:
            return {'error': e.args[0]}, 400
