class Password:
    def __init__(self, value: str):
        self._set_value(value)

    @property
    def value(self) -> str:
        return self._value

    def _set_value(self, value: str):
        if len(value) < 6:
            raise ValueError({'password': 'Requires six or more characters'})
        self._value = value
