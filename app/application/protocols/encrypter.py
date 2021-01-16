from typing import Protocol
from abc import abstractmethod


class Encrypter(Protocol):
    @abstractmethod
    def compare(self, pw_hash: str, password: str) -> bool:
        raise NotImplemented

    @abstractmethod
    def hash(self, password: str) -> str:
        raise NotImplemented
