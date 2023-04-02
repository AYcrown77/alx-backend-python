#!/usr/bin/env python3
"""Type-anntated function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Retrurns the sum of floats and integers
    args:
        mxd_lst: list of floats and integers
    """

    return sum(mxd_lst)
