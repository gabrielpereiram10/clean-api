from typing import Protocol
from abc import abstractmethod


class HashComparer(Protocol):
    @abstractmethod
    def compare(self, value_hash: str, value: str) -> bool:
        raise NotImplemented
