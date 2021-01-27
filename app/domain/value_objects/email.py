class Email:
    def __init__(self, value: str):
        self._set_value(value)

    @property
    def value(self) -> str:
        return self._value

    def _set_value(self, email: str):
        if not email:
            raise ValueError
        self._value = email
