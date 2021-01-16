from app.main.config.jwt import jwt, key, algorithm
from app.application.protocols.cryptography.encrypter import Encrypter


class PyJWTAdapter(Encrypter):
    def encrypt(self, value: str) -> str:
        return jwt.encode({'identity': value}, key, algorithm).decode('utf-8')
