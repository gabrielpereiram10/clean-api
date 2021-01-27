from app.domain.value_objects.email import Email
from app.domain.value_objects.password import Password
from app.domain.usecases.auth import AuthenticationUseCase

from app.application.protocols.user_repository import UserRepository
from app.application.protocols.cryptography.hash_checker import HashChecker


class AuthenticationService(AuthenticationUseCase):
    def __init__(self, user_repository: UserRepository, hash_checker: HashChecker):
        self.user_repository = user_repository
        self.hash_checker = hash_checker

    def authenticate(self, email: str, password: str) -> bool:
        email = Email(email)
        password = Password(password)
        user = self.user_repository.find_by_email(email.value)
        if not user:
            raise ValueError({'email': 'User does not exist!'})
        if not self.hash_checker.check(user.password, password.value):
            raise ValueError({'password': 'Invalid!'})
        return True
