from app.application.services.authentication import AuthenticationService

from app.presentation.controllers.authentication import AuthenticationController

from app.infra.db.fake_db.fake_user_repository import FakeUserRepository
from app.infra.cryptography.encrypt_adapter import EncryptAdapter
from app.infra.cryptography.token_adapter import TokenAdapter


def create_authentication_controller() -> AuthenticationController:
    use_case = AuthenticationService(FakeUserRepository(), EncryptAdapter())
    return AuthenticationController(use_case, TokenAdapter())
