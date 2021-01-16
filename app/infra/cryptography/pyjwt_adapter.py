import os
import jwt

from app.application.protocols.cryptography.encrypter import Encrypter


class PyJWTAdapter(Encrypter):
    def encrypt(self, value: str) -> str:
        key = os.environ.get('JWT_SECRET_KEY')
        algorithm = os.environ.get('ALGORITHM')
        return jwt.encode({'identity': value}, key, algorithm).decode('utf-8')
