from werkzeug.security import check_password_hash, generate_password_hash

from app.application.protocols.encrypter import Encrypter


class EncryptAdapter(Encrypter):
    def compare(self, pw_hash: str, password: str) -> bool:
        return check_password_hash(pw_hash, password)

    def hash(self, password: str) -> str:
        return generate_password_hash(password)
