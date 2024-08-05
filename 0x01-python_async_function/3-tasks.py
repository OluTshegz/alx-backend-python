#!/usr/bin/env python3
"""
This module provides a function to
create an asyncio Task from `wait_random`.
"""

import asyncio
# from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task for the `wait_random`
    coroutine with the given max_delay.

    Parameters:
    max_delay (int): The maximum delay in seconds
    for the wait_random coroutine.

    Returns:
    asyncio.Task: An asyncio Task object representing the
    running task for the wait_random coroutine.
    """
    # Creates a `new` `asyncio` task to execute the `wait_random`
    # coroutine with the specified `max_delay` and returns the task object.
    return asyncio.create_task(wait_random(max_delay))
