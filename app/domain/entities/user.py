from app.domain.value_objects.email import Email
from app.domain.value_objects.password import Password


class User:
    def __init__(self, email: Email, password: Password):
        self._set_email(email)
        self._set_password(password)

    @property
    def email(self):
        return self._email

    def _set_email(self, value: Email):
        self._email = value

    @property
    def password(self):
        return self._password

    def _set_password(self, value: Password):
        self._password = value
