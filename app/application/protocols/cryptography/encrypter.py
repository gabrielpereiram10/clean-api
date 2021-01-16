from typing import Protocol
from abc import abstractmethod


class Encrypter(Protocol):
    @abstractmethod
    def encrypt(self, value: str) -> str:
        raise NotImplemented
