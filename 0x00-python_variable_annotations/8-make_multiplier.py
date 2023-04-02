#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes
    a float multiplier as argument and
returns a function that multiplies a float by multiplier"""

from atyping import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): multiplier

    Return:
        flaot: function that multiplies a float  by multiplier
    """
    return lambda x: x * multiplier
