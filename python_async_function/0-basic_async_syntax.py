#!/usr/bin/env python3
""" A basic async function. """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ creates a delay between 0 and max delay. """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
