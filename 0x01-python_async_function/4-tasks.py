#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new
    function task_wait_n"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks_done = []
    delays_time = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks_done.append(task)

    for task in asyncio.as_completed((tasks_done)):
        delay = await task
        delays_time.append(delay)

    return delays_time
