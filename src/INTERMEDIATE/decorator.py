"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""

from typing import Callable, TypeVar

TCallable = TypeVar("TCallable", bound=Callable)


def decorator(func: TCallable) -> TCallable:
    return func
