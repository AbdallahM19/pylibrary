"""print_class.py"""

import asyncio
from time import time
from functools import wraps
from typing import Callable


# create two func print each args and kwargs
def print_args(*args) -> None:
    """A decorator that prints the function arguments"""
    if args:
        print("Arguments:")
        for arg in args:
            print(f"- {arg}")

def print_kwargs(**kwargs) -> None:
    """A decorator that prints the function keyword arguments"""
    if kwargs:
        print("Keyword Arguments:")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")

# create func print each var in list
def print_list(lst) -> None:
    """A decorator that prints each variable in a list"""
    if lst:
        print("List:")
        for var in lst:
            print(f"- {var}")


def print_func_time(func: Callable) -> Callable:
    """Decorator to measure and print the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f}s to execute")
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

    def __call__(self, func: Callable) -> Callable:
        """A decorator that prints the execution time of a function"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            async def async_inner():
                start_time = time()
                result = await func(*args, **kwargs)
                end_time = time()
                self._print_info(func, args, kwargs, result, end_time - start_time)
                return result

            def sync_inner():
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                self._print_info(func, args, kwargs, result, end_time - start_time)
                return result

            if asyncio.iscoroutinefunction(func):
                return async_inner()
            return sync_inner()

        return wrapper

    def _print_info(self, func, args, kwargs, result, elapsed_time) -> None:
        """Helper method to print function information."""
        print(f"Function {func.__name__}")

        if self.show_args:
            print_args(*args)
        if self.show_kwargs:
            print_kwargs(**kwargs)
        if self.show_time:
            print(f"Time: {elapsed_time:.4f}s")
        if self.show_return:
            print(f"Return Value: {result}")

    @staticmethod
    def print_all_info(func: Callable) -> Callable:
        """Decorator to print all function details."""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time()
            result = await func(*args, **kwargs)
            elapsed_time = time() - start_time
            print(
                f"Function {func.__name__}\n\
                    Time: {elapsed_time:.4f}s\n\
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
