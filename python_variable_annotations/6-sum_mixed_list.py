#!/usr/bin/env python3
"""return the sum of a mixed list with ints and floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Add float and int numbers and return their sum.

    Args:
    input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the numbers.
    """
    return sum(mxd_lst)
