from typing import Protocol
from abc import abstractmethod


class AuthenticationUseCase(Protocol):
    @abstractmethod
    def authenticate(self, email: str, password: str) -> bool:
        raise NotImplemented
