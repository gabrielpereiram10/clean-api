from werkzeug.security import check_password_hash, generate_password_hash

from app.application.protocols.cryptography.hasher import Hasher
from app.application.protocols.cryptography.hash_checker import HashChecker


class WerkzeugSecurityAdapter(Hasher, HashChecker):
    def check(self, value_hash: str, value: str) -> bool:
        return check_password_hash(value_hash, value)

    def hash(self, value: str) -> str:
        return generate_password_hash(value)
