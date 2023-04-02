#!/usr/bin/env python3
"""
Annotate fucnction and return values with type-annotations
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return element lenght
    
    Args:
        lst (Iterable[Sequence]): iterable to be counted

    Returns:
        List[Tuple[Sequence, int]]: length of iterable
    """
    return [(i, len(i)) for i in lst]
