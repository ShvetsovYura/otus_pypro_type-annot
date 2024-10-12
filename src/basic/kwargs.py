"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""

from typing import TypedDict, Unpack


class Options(TypedDict):
    a: int
    b: str


def foo(**kwargs: Unpack[Options]): ...
