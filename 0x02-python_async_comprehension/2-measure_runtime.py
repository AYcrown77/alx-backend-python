#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start
