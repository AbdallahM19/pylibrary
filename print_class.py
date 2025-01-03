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


def _print_info(func, args, kwargs, result, elapsed_time) -> None:
    """Helper method to print function information."""
    print(f"Function {func.__name__}")

    print_args(*args)
    print_kwargs(**kwargs)

    print(f"Time: {elapsed_time:.4f}s")
    print(f"Return Value: {result}")


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
    def __init__(self):
        pass

    def __call__(self, func: Callable) -> Callable:
        """A decorator that prints the execution time of a function"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            async def async_inner():
                start_time = time()
                result = await func(*args, **kwargs)
                elapsed_time = time() - start_time
                _print_info(func, args, kwargs, result, elapsed_time)
                return result

            def sync_inner():
                start_time = time()
                result = func(*args, **kwargs)
                elapsed_time = time() - start_time
                _print_info(func, args, kwargs, result, elapsed_time)
                return result

            if asyncio.iscoroutinefunction(func):
                return async_inner()
            return sync_inner()

        return wrapper

    @staticmethod
    def print_all_func_info(func: Callable) -> Callable:
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
    def print_each_args_and_kwargs(func: Callable) -> Callable:
        """Decorator to print each argument and keyword argument of a function"""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            await print_args(*args)
            await print_kwargs(**kwargs)
            return await func(*args, **kwargs)
        return wrapper
