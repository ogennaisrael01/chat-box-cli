import functools
import os
import logging

logger = logging.getLogger(__name__)

max_retries = os.getenv("max_retries", 3)

def retry_on_failure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if max_retries is None:
            raise ValueError("max retries cannot be empty")
        for attempts in range(1, int(max_retries)+1):
            try:
                response = func(*args, **kwargs)
                return response
            except Exception:
                logging.exception(f"Failed to fetch request, retrying on attempt {attempts}....", exc_info=True)  
        logger.info("Max attempts exceeded. \nExecution failed.")
        raise ValueError(f"Max Attempt Exceeded: {attempts} attempts")   
    return wrapper