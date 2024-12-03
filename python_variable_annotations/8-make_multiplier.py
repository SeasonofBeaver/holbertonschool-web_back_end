#!/usr/bin/env python3
"""a multiplier function for floats"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that multiplies a float with a multiplier.

    Args:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies
    a float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
