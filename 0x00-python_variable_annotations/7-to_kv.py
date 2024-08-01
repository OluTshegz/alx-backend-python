#!/usr/bin/env python3
"""
This module provides a function to create
a tuple from a string and an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and
    the square of an int or float as a float.

    Parameters:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The number to be squared.

    Returns:
    Tuple[str, float]: A tuple where the first element
                    is k and the second element
                    is the square of v as a float.
    """
    return (k, float(v ** 2))
