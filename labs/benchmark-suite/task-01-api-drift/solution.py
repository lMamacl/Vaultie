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
        # BUG: Legacy method name and missing required 'schema_version' key
        # In modern API contract, serialization must return dict with schema_version: 2 and validated fields
        return {
            "id": self.user_id,
            "name": self.username,
            "email": self.email
        }
