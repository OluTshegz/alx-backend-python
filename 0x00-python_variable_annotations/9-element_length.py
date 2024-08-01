#!/usr/bin/env python3
"""
This module provides a function that returns
the length of elements in an iterable.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing
    elements and their lengths.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing
                            sequence elements.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple
                                contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
