#!/usr/bin/env python3
""" Asyncronous generator """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    random numbers to create random async
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
