#!/usr/bin/env python3
"""function for element length"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with an element of the list and its length.

    Args:
    lst (Iterable[Sequence]): The list.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where
    with an element of the list and its length.
    """
    return [(i, len(i)) for i in lst]
