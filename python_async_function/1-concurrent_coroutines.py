#!/usr/bin/env python3
"""this is the module for the second task"""
import asyncio
from typing import List
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """this is the method"""
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(l)]
    return finish
