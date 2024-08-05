#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine
that spawns multiple `wait_random` tasks.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns `wait_random`
    `n` times with a specified `max_delay`.

    Parameters:
    n (int): The number of times to call `wait_random`.
    max_delay (int): The maximum delay in seconds
    for each `wait_random` call.

    Returns:
    List[float]: A list of all the delays in ascending order.
    """

    # [1]
    # # Create a list of coroutines using a generator expression
    # coroutines = (wait_random(max_delay) for _ in range(n))

    # # Execute the coroutines concurrently and gather their results
    # delays = await asyncio.gather(*coroutines)

    # # Return the delays sorted in ascending order
    # return sorted(delays)

    # [2]
    # # Create a list of tasks using list comprehension
    # tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # # Execute the tasks concurrently and gather their results in a list
    # delays = [await task for task in asyncio.as_completed(tasks)]

    # # Return the list of delays
    # return delays

    # [3]
    # Create a list to store the created tasks
    tasks = []
    # Create a list to store the results (delays) of the tasks
    delays = []

    # Create `n` tasks sequentially and store them in a list
    for i in range(n):
        # Create a task and append it to the tasks list
        task = wait_random(max_delay)
        tasks.append(task)

    # Execute tasks concurrently and gather their results sequentially
    for task in asyncio.as_completed(tasks):
        # Wait for the task to complete and
        # append the result to the delays list
        delay = await task
        delays.append(delay)

    # Return the list of delays
    return delays
