#!/usr/bin/env python3
"""
This module contains a coroutine `measure_runtime` which
executes `async_comprehension` four times in parallel
and measures the total runtime.

`time.time()` might be used to get the current time
or measure elapsed time over a longer period.
`time.perf_counter()` is better for measuring precise intervals
and performance testing, as it provides higher resolution
and is not affected by clock adjustments.
For performance measurements and benchmarking, `time.perf_counter()`
is generally preferred due to its higher precision and stability."""

import asyncio
import time
# from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes `async_comprehension` four times in parallel
    and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_perf = time.perf_counter()
    # await asyncio.gather(*(async_comprehension() for i in range(4)))
    # task = [async_comprehension() for i in range(4)]
    # await asyncio.gather(*task)
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_perf = time.perf_counter()
    return (end_perf - start_perf)
