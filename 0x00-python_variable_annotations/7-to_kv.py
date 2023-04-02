#!/usr/bin/env python3
"""
Type-annoted function to_kv that takes
    a string k and 
    an int OR float v
as arguments and returns tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v:  Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of a string and a float

    Args:
        k (str): string element
        v (Union[int, float]): int or float element

    returns:
        Tuple: tuple of arguments k and v
    """
    return (k, v**2)
