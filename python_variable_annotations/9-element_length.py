#!/usr/bin/env python3
"""function for element length"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Return a list of tuples with an element of the list and its length.

    Args:
    lst (List[str]): The list.

    Returns:
    List[Tuple[str, int]]: A list of tuples where
    with an element of the list and its length.
    """
    return [(i, len(i)) for i in lst]
