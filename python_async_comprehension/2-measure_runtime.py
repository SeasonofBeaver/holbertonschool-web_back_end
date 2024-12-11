#!/usr/bin/env python3
""" program to measure the runtime. """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measuring the time it takes to run 
    all coroutines at the same time.
    """

    startTime = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    endTime = time.perf_counter()
    return endTime - startTime
