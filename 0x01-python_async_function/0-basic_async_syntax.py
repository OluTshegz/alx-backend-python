#!/usr/bin/env python3
"""
This module provides an asynchronous
coroutine to wait for a random delay.
"""

import asyncio
import random
# from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay
    between 0 and max_delay seconds and returns it.

    Parameters:
    max_delay (int, optional): The maximum delay in seconds.
    Defaults to 10.

    Returns:
    float: The actual delay time.
    """
    # Generate a random delay between 0 and `max_delay`

    # more direct and efficient for generating a random
    # floating-point number within a specific range
    delay: float = random.uniform(0, max_delay)

    # Potential for Inaccuracy: Multiplying a random float
    # between 0 and 1 by `max_delay` might not always produce
    # a value that reaches the exact `max_delay`
    # due to floating-point precision
    # delay: float = random.random() * max_delay

    # Suspend the coroutine for the specified delay
    await asyncio.sleep(delay)

    # Return the actual delay
    return delay
