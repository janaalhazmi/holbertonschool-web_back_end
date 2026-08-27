#!/usr/bin/env python3
"""this is a modul for the first task"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """this is the method"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
