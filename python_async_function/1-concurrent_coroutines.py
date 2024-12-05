#!/usr/bin/env python3
import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """ creates a delay between 0 and max delay. """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ create a list of multiple delays made. """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        for i, existing in enumerate(delays):
            if delay < existing:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return sorted(delays)
