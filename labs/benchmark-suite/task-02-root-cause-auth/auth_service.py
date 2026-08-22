"""
Downstream Service: Auth Controller
Uses TokenGenerator.
"""
from token_generator import TokenGenerator

class AuthService:
    def __init__(self):
        # BUG: Instantiating a new generator with different secret default or unshared instance
        self.generator = TokenGenerator()

    def login(self, username: str) -> str:
        return self.generator.generate_token(username)

    def authenticate_request(self, token: str) -> bool:
        # Calls verification on upstream generator
        # If upstream generator is broken or instance is recreated with empty secret, fails.
        return self.generator.verify_token(token)
