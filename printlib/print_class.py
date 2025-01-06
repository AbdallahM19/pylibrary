"""print_class.py"""

import asyncio
from time import time
from functools import wraps
from typing import Callable, Any

# count time that take func to execute
# async def time_count(func: callable):
#     """Decorator to count time that take func to execute"""
#     start_time = time()
#     await func
#     elapsed_time = time() - start_time
#     return elapsed_time

# function to return async or sync
async def async_or_sync(func: Callable, *args, **kwargs) -> Any:
    """Execute a function, whether synchronous or asynchronous."""
    if asyncio.iscoroutinefunction(func):
        return await func(*args, **kwargs)
    return func(*args, **kwargs)

# create two func print each args and kwargs
def print_args(*args) -> None:
    """A decorator that prints the function arguments"""
    if args:
        print("Arguments:")
        for arg in args:
            print(f"- {arg}")
    else:
        print("Arguments: No")

def print_kwargs(**kwargs) -> None:
    """A decorator that prints the function keyword arguments"""
    if kwargs:
        print("Keyword Arguments:")
        for key, value in kwargs.items():
            print(f"- {key}: {value}")
    else:
        print("Keyword Arguments: No")

# create func print each var in list
def print_list(lst) -> None:
    """A decorator that prints each variable in a list"""
    if lst:
        print("List:")
        for var in lst:
            print(f"- {var}")
    else:
        print("List: No")


async def _print_info(func, args, kwargs, result, elapsed_time) -> None:
    """Helper method to print function information."""
    print(f"Function {func.__name__}")

    print_args(*args)
    print_kwargs(**kwargs)

    print(f"Time: {elapsed_time:.4f}s")
    print(f"Return Value: {result}")


class PrintFuncInfo():
    """A class that provides a decorator to print the execution time of a function."""
    def __init__(self):
        pass

    def __call__(self, func: Callable) -> Callable:
        """A decorator that prints the execution time of a function"""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time()
            result = await async_or_sync(func, *args, **kwargs)
            elapsed_time = time() - start_time
            await _print_info(func, args, kwargs, result, elapsed_time)
            return result
        return wrapper

    @staticmethod
    def print_func_time(func: Callable) -> Callable:
        """Decorator to measure and print the execution time of a function."""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time()
            result = await async_or_sync(func, *args, **kwargs)
            elapsed_time = time() - start_time
            print(f"Function {func.__name__} took {elapsed_time:.4f}s to execute")
            return result
        return wrapper

    @staticmethod
    def print_all_func_info(func: Callable) -> Callable:
        """Decorator to print all function details."""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time()
            result = await async_or_sync(func, *args, **kwargs)
            elapsed_time = time() - start_time
            await _print_info(func, args, kwargs, result, elapsed_time)
            return result
        return wrapper

    @staticmethod
    def print_each_args_and_kwargs(func: Callable) -> Callable:
        """Decorator to print each argument and keyword argument of a function"""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            print_args(*args)
            print_kwargs(**kwargs)
            return await async_or_sync(func, *args, **kwargs)
        return wrapper
