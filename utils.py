import time
from functools import wraps


def measure_execution_time(func):
    """
    A decorator function that measures the execution time of a given function.

    Args:
    - func: The function to measure execution time for.

    Returns:
    - wrapper: The wrapped function that measures execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result

    return wrapper
