import unittest
from unittest.mock import patch, MagicMock
from solution import execute_with_retry

class TestExponentialBackoffJitter(unittest.TestCase):
    def test_successful_on_first_try(self):
        mock_fn = MagicMock(return_value="OK")
        result = execute_with_retry(mock_fn, max_retries=3, base_delay=0.1)
        self.assertEqual(result, "OK")
        self.assertEqual(mock_fn.call_count, 1)

    @patch("time.sleep")
    def test_exponential_backoff_applied(self, mock_sleep):
        failing_fn = MagicMock(side_effect=[ValueError("Fail 1"), ValueError("Fail 2"), "Success"])
        result = execute_with_retry(failing_fn, max_retries=4, base_delay=1.0)
        
        self.assertEqual(result, "Success")
        self.assertEqual(failing_fn.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)
        
        # Verify delays are increasing (Exponential Backoff with Full Jitter or Equal Jitter)
        # Attempt 1: delay in range [0, 1.0 * 2^0] = [0, 1.0] or average > 0
        # Attempt 2: delay in range [0, 1.0 * 2^1] = [0, 2.0]
        delays = [call.args[0] for call in mock_sleep.call_args_list]
        self.assertEqual(len(delays), 2)
        # Attempt 1 base should be ~1.0, Attempt 2 should be ~2.0 (>= 1.5)
        self.assertGreater(delays[1], delays[0], "Second retry delay must be exponentially larger than first retry delay")
        self.assertGreaterEqual(delays[1], 1.5, "Second retry delay must scale with 2^1 backoff factor")


if __name__ == "__main__":
    unittest.main()
