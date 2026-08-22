import unittest
from auth_service import AuthService
from token_generator import TokenGenerator

class TestAuthenticationPersistence(unittest.TestCase):
    def test_session_token_validation(self):
        auth = AuthService()
        token = auth.login("engineer_01")
        
        # Immediate verification
        self.assertTrue(auth.authenticate_request(token), "Token must validate immediately after login")
        
        # Cross-instance verification (simulating worker restart with same secret)
        verifier_service = AuthService()
        self.assertTrue(verifier_service.authenticate_request(token), "Token must validate across independent service instances sharing the standard secret")

    def test_tampered_token_rejection(self):
        auth = AuthService()
        token = auth.login("engineer_02")
        tampered = token[:-4] + "ffff"
        self.assertFalse(auth.authenticate_request(tampered), "Tampered token must be strictly rejected")

if __name__ == "__main__":
    unittest.main()
