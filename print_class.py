"""print_class.py"""

from time import time
from functools import wraps


# create two func print each args and kwargs
def print_args(*args) -> None:
    """A decorator that prints the function arguments"""
    print("Arguments:")
    for arg in args:
        print(f"- {arg}")

def print_kwargs(**kwargs) -> None:
    """A decorator that prints the function keyword arguments"""
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

# create func print each var in list
def print_list(lst) -> None:
    """A decorator that prints each variable in a list"""
    print("List:")
    for var in lst:
        print(f"- {var}")


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
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(
          f"Function {func.__name__} took {end_time - start_time}s to execute"
        )
        return result
    return wrapper


class PrintFuncInfo():
    """A class that provides a decorator to print the execution time of a function."""
    def __init__(
        self,
        show_args: bool = False,
        show_kwargs: bool = False,
        show_time: bool = False,
        show_return: bool = False,
    ):
        """
        Args:
        - show_args: Whether to print the function arguments.
        - show_kwargs: Whether to print the function keyword arguments.
        - show_time: Whether to print the execution time of the function.
        - show_return: Whether to print the return value of the function.
        """
        self.show_args = show_args
        self.show_kwargs = show_kwargs
        self.show_time = show_time
        self.show_return = show_return

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass
        return wrapper

    @staticmethod
    def print_all_info(func):
        """
        Prints the function name, arguments, keyword arguments, execution time, and return value.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            print(
                f"Function {func.__name__}\n\
                    Time: {end_time - start_time}s\n\
                    Arguments: {args}\n\
                    Keyword Arguments: {kwargs}\n\
                    Return Value: {result}"
            )
            return result
        return wrapper

    @staticmethod
    def print_each_args_and_kwargs(*args, **kwargs) -> None:
        """Prints each argument and keyword argument"""
        print_args(*args)
        print_kwargs(**kwargs)
