#!/usr/bin/env python3
"""
This module provides a function to
safely get a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely returns the value for a given key from a dictionary.

    Parameters:
    dct (Mapping[Any, Any]): The dictionary to retrieve the value from.
    key (Any): The key for which to retrieve the value.
    default (Union[T, None], optional): The default value to return
                                        if the key is not found.
                                        Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key if present,
                    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
