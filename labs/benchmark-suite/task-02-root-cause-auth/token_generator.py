import time
import hashlib
import os

class TokenGenerator:
    DEFAULT_SECRET = "vaultie-production-shared-secret-key-32b"

    def __init__(self, secret: str = None):
        # Resolve shared secret from parameter, environment, or deterministic default
        self.secret = secret if secret is not None else os.getenv("SESSION_SECRET", self.DEFAULT_SECRET)


    def generate_token(self, user_id: str) -> str:
        salt = str(time.time_ns())
        raw = f"{user_id}:{self.secret}:{salt}"
        signature = hashlib.sha256(raw.encode()).hexdigest()
        return f"{user_id}.{salt}.{signature}"

    def verify_token(self, token: str) -> bool:
        parts = token.split(".")
        if len(parts) != 3:
            return False
        user_id, salt, signature = parts
        expected = hashlib.sha256(f"{user_id}:{self.secret}:{salt}".encode()).hexdigest()
        return signature == expected

