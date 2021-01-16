from app.main.config.jwt import jwt, key, algorithm
from app.presentation.protocols.token_generator import TokenGenerator


class TokenAdapter(TokenGenerator):
    def generate(self, identity: str) -> str:
        return jwt.encode({'identity': identity}, key, algorithm).decode('utf-8')
