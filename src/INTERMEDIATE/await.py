"""
TODO:

`run_async` takes an awaitable integer.
"""

from typing import Coroutine


def run_async(val: Coroutine[None, None, int]) -> None: ...
