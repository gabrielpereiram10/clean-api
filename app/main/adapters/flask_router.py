from typing import Callable
from flask import Request

from app.presentation.protocols.controller import Controller
from app.presentation.protocols.http import HttpRequest, HttpResponse


def flask_router_adapter(controller: Controller) -> Callable[[Request], HttpResponse]:
    def router(req: Request) -> HttpResponse:
        http_request = HttpRequest(dict(req.json))
        return controller.handle(http_request)
    return router
