from app.domain.entities.email import Email
from app.domain.entities.password import Password
from app.domain.usecases.auth import AuthenticationUseCase

from app.application.protocols.user_repository import UserRepository
from app.application.protocols.cryptography.hash_comparer import HashComparer


class AuthenticationService(AuthenticationUseCase):
    def __init__(self, user_repository: UserRepository, hash_comparer: HashComparer):
        self.user_repository = user_repository
        self.hash_comparer = hash_comparer

    def authenticate(self, email: str, password: str) -> bool:
        email = Email(email)
        password = Password(password)
        user = self.user_repository.find_by_email(email.value)
        if not user:
            raise ValueError({'email': 'User does not exist!'})
        if not self.hash_comparer.compare(user.password, password.value):
            raise ValueError({'password': 'Invalid!'})
        return True
