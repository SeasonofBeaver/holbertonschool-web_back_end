#!/usr/bin/env python3
"""function to create a new list to wait a certain amount of time. """

import asyncio
from typing import List


wait_random = __import__('1-concurrent_coroutines').wait_random


async def task_wait_random(n: int, max_delay: int) -> List[float]:
    """ return a list of sorted delays """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
