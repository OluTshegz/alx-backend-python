#!/usr/bin/env python3
"""
This module provides a function
that creates a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies
    a float by a given multiplier.

    Parameters:
    multiplier (float): The multiplier to use.

    Returns:
    Callable[[float], float]: A function that takes a float and
                            returns it multiplied by the multiplier.
    """
    def multiply(n: float) -> float:
        """Multiplies the input float by the multiplier."""
        return n * multiplier

    return multiply
