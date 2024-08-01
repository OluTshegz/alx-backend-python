#!/usr/bin/env python3
"""
This module provides a function to
sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list
    containing integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]):
    A list containing integers and floats.

    Returns:
    float: The sum of all numbers in the list as a float.
    """
    return sum(mxd_lst)
