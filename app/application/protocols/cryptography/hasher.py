from typing import Protocol
from abc import abstractmethod


class Hasher(Protocol):
    @abstractmethod
    def hash(self, value: str) -> str:
        raise NotImplemented