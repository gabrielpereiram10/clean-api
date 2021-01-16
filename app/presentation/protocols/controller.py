from typing import Protocol
from abc import abstractmethod

from app.presentation.protocols.http import HttpResponse, HttpRequest


class Controller(Protocol):
    @abstractmethod
    def handle(self, req: HttpRequest) -> HttpResponse:
        raise NotImplemented
