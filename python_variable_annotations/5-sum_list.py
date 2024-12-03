#!/usr/bin/env python3
"""a function that adds the numbers together."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Add float numbers and return their sum.

    Args:
    input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the numbers.
    """
    return sum(input_list)
