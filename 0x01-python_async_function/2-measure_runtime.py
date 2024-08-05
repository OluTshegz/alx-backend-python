#!/usr/bin/env python3
"""
This module provides a function to measure
the execution time of the `wait_n` coroutine.
"""

import asyncio
import time
# from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


# Measure the execution time for running `n` tasks concurrently
def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    `wait_n(n, max_delay)` and returns the
    average time per call.
    Measures the average execution time of
    running `n` tasks concurrently.

    Args/Parameters:
    n (int): The number of tasks to run or
    times to call `wait_n`.
    max_delay (int): The maximum delay in seconds
    for each task or `wait_random` call.

    Returns:
    float: The average execution time per task or call (in seconds).
    """

    # Start time measurement
    start_time = time.time()
    # Run the asynchronous function using asyncio.run
    asyncio.run(wait_n(n, max_delay))
    # Stop time measurement
    stop_time = time.time()
    # Calculate total execution time
    total_time = stop_time - start_time
    # Calculate average execution time per task
    average_time = total_time / n
    # Return the average time
    return average_time
