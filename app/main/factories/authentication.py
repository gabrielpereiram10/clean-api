from app.application.services.authentication import AuthenticationService

from app.presentation.controllers.authentication import AuthenticationController

from app.infra.db.fake_db.fake_user_repository import FakeUserRepository
from app.infra.cryptography.werkzeug_security_adapter import WerkzeugSecurityAdapter
from app.infra.cryptography.pyjwt_adapter import PyJWTAdapter


def create_authentication_controller() -> AuthenticationController:
    use_case = AuthenticationService(FakeUserRepository(), WerkzeugSecurityAdapter())
    return AuthenticationController(use_case, PyJWTAdapter())
