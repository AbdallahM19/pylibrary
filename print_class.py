from time import time, sleep
from functools import wraps

def print_func_time(func):
    """
    Decorator:
    - Prints the time taken by the function to execute
    - Return the elapsed time

    Args:
        func: The function to be decorated.

    Returns:
        A wrapper function that measures and prints the execution time of the original function,
        then returns the elapsed time.

    Example:
        @print_func_time
        def my_function():
            # Function code here
            pass

        result = my_function()
        print(f"Function executed in {result} seconds")
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
      start_time = time()
      result = func(*args, **kwargs)
      end_time = time()
      print(
        f"Function {func.__name__} took {end_time - start_time} seconds to execute"
      )
      return result
    return wrapper


def sleeptime():
    sleep(2)

sleeptime()