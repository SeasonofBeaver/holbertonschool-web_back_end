#!/usr/bin/env python3
"""gets a union and returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    changes the float or int into a squared version.

    Args:
    k (str): the string
    v (Union[int, float]): The union of float or int.

    Returns:
    Tuple[str, float]: The string and then the float or int as square.
    """
    return (k, float(v**2))
