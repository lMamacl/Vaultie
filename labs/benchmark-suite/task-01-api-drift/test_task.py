import unittest
from solution import UserProfile

class TestUserProfileModernAPI(unittest.TestCase):
    def test_modern_schema_compliance(self):
        user = UserProfile(user_id=101, username="alex_dev", email="alex@vaultie.local", is_active=True)
        data = user.serialize_payload()
        
        # Modern contract assertions
        self.assertIn("schema_version", data, "Payload must include 'schema_version' (v2)")
        self.assertEqual(data["schema_version"], 2)
        self.assertEqual(data["user_id"], 101, "Key must be 'user_id', not legacy 'id'")
        self.assertEqual(data["username"], "alex_dev", "Key must be 'username', not legacy 'name'")
        self.assertEqual(data["is_active"], True, "Payload must preserve 'is_active' boolean flag")

if __name__ == "__main__":
    unittest.main()
