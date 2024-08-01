#!/usr/bin/env python3
"""
This module provides a function to zoom
into a tuple by repeating its elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list with elements from the
    tuple repeated according to the factor.

    Parameters:
    lst (Tuple[int, ...]): The tuple to zoom into.
    factor (int, optional): The number of times to
                            repeat each element.
                            Defaults to 2.

    Returns:
    List[int]: A list with repeated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
