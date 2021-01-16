from typing import Protocol, Union
from abc import abstractmethod

from app.application.models.user import UserModel


class UserRepository(Protocol):
    @abstractmethod
    def find_by_email(self, email: str) -> Union[UserModel, None]:
        raise NotImplemented
