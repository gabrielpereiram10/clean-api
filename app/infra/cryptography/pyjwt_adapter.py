import os
import jwt

from app.application.protocols.cryptography.encrypter import Encrypter


class PyJWTAdapter(Encrypter):
    def __init__(self):
        self._key = os.environ.get('JWT_SECRET_KEY')
        self._algorithm = os.environ.get('ALGORITHM')

    def encrypt(self, value: str) -> str:
        return jwt.encode({'identity': value}, self._key, self._algorithm).decode('utf-8')
