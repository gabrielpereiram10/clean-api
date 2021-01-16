from app.domain.entities.email import Email
from app.domain.entities.password import Password
from app.domain.usecases.auth import AuthenticationUseCase

from app.application.protocols.user_repository import UserRepository
from app.application.protocols.encrypter import Encrypter


class AuthenticationService(AuthenticationUseCase):
    def __init__(self, user_repository: UserRepository, encrypter: Encrypter):
        self.user_repository = user_repository
        self.encrypter = encrypter

    def authenticate(self, email: str, password: str) -> bool:
        email = Email(email)
        password = Password(password)
        user = self.user_repository.find_by_email(email.value)
        if not user:
            raise ValueError({'email': 'User does not exist!'})
        if not self.encrypter.compare(user.password, password.value):
            raise ValueError({'password': 'Invalid!'})
        return True
