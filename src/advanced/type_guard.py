"""
TODO:

`is_string` determines whether the input value is a string.
Your job is to make the type checker be aware of this information.
"""

from typing import Any, TypeGuard


def is_string[T](value: T) -> TypeGuard[str]: # pyright: ignore[reportInvalidTypeVarUse]
    return isinstance(value, str)
