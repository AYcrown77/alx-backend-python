#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random time"""
    waiting_time = random.random() * max_delay
    await asyncio.sleep(waiting_time)
    return waiting_time
