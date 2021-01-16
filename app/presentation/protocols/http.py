from typing import Dict, Any, Union, Tuple


class HttpRequest:
    def __init__(self, data: Dict = None):
        self.data = data


HttpResponse = Union[int, Tuple[Any, int]]
