class AuthInputModel:
    def __init__(self, email: str, password: str):
        self._set_email(email)
        self._set_password(password)

    @property
    def email(self):
        return self._email

    def _set_email(self, value: str):
        if not isinstance(value, str):
            raise TypeError({'email': 'Requires string type.'})
        self._email = value

    @property
    def password(self):
        return self._password

    def _set_password(self, value: str):
        if not isinstance(value, str):
            raise TypeError({'password': 'Requires string type.'})
        self._password = value


class UserModel:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
