#!/usr/bin/env python3
"""helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple with a beginning and end index."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
