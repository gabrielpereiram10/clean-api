from typing import Protocol
from abc import abstractmethod


class HashChecker(Protocol):
    @abstractmethod
    def check(self, value_hash: str, value: str) -> bool:
        raise NotImplemented
