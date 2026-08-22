import time
import random
from typing import Callable, Any

def execute_with_retry(fn: Callable[[], Any], max_retries: int = 3, base_delay: float = 0.5) -> Any:
    """
    Executes a callable with exponential backoff and jitter on exceptions.
    """
    attempts = 0
    while attempts < max_retries:
        try:
            return fn()
        except Exception as e:
            attempts += 1
            if attempts >= max_retries:
                raise e
            # Exponential backoff: base_delay * 2^(attempts - 1)
            backoff = base_delay * (2 ** (attempts - 1))
            # Equal jitter: half deterministic, half random jitter
            jitter = random.uniform(0, 0.1 * backoff)
            delay = backoff + jitter
            time.sleep(delay)

