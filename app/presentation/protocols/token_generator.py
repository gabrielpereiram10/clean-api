from typing import Protocol
from abc import abstractmethod


class TokenGenerator(Protocol):
    @abstractmethod
    def generate(self, identity: str) -> str:
        raise NotImplemented
