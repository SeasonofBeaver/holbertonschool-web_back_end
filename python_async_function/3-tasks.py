#!/usr/bin/env python3
"""function to create a new instance to wait a certain amount of time. """

import asyncio


wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ create a new task to wait a random amount of time """
    return asyncio.create_task(wait_random(max_delay))
