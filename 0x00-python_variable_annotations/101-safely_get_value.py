#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function"""

from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T,
                                    None] = None) -> Union[Any,
                                                           T]:
    """safely reutrn value of key in dict or default

    Args:
        dct (Mapping): dictionary to be checked
        key (Any): key to be checked
        default (Union[TypeVar, None], optional): value to be retrieved.
                                                Defaults to None.

    Returns:
        Union[Any, TypeVar]: value if exists or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
