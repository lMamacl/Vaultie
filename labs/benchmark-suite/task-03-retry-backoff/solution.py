"""
Task 03: Exponential Backoff with Jitter
Naive implementation: Linear fixed delay, no jitter, unbounded retries causing stampedes.
"""
import time
from typing import Callable, Any

def execute_with_retry(fn: Callable[[], Any], max_retries: int = 3, base_delay: float = 0.5) -> Any:
    # BUG: Fixed linear sleep without exponential calculation and without jitter
    attempts = 0
    while attempts < max_retries:
        try:
            return fn()
        except Exception as e:
            attempts += 1
            if attempts >= max_retries:
                raise e
            time.sleep(base_delay)  # Linearly sleeping without backoff
