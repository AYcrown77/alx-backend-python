#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay."""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait random n number of times with the specified max_delay"""
    tasks_done = []
    delay_times = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks_done.append(task)

    for task in asyncio.as_completed((tasks_done)):
        delay = await task
        delay_times.append(delay)
    return delay_times
