"""
Task 01: API Drift (Simulating Pydantic / Serialization Modernization)
The current solution uses legacy serialization methods that fail modern validation contracts.
"""

class UserProfile:
    def __init__(self, user_id: int, username: str, email: str, is_active: bool = True):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.is_active = is_active

    def serialize_payload(self) -> dict:
        return {
            "schema_version": 2,
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
        }
