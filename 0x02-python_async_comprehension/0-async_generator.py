#!/usr/bin/env python3
"""
This module contains a coroutine called
`async_generator` which yields random numbers.
AsyncGenerator is used specifically for
asynchronous generator functions.
The annotation `AsyncGenerator[float, None]`
indicates that the async generator yields float
values and doesn't accept any values sent to it (None).
The third argument, which indicates the return type of the generator,
is optional in `AsyncGenerator` because asynchronous generators
do not support the return statement directly as synchronous generators do.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a
    random float between 0 and 10.

    This coroutine will loop 10 times,
    each time asynchronously waiting 1 second
    before yielding a random float.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator
        that yields random floats.
    """
    # `_` is a throwaway variable, an unused loop index,
    # holding current iteration index (ranging from 0 to 9),
    # yielding only sequential numbers, not random.
    for _ in range(10):
        await asyncio.sleep(1)
        # yield random.random() * 10
        yield random.uniform(0, 10)
