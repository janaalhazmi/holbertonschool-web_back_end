#!/usr/bin/env python3
"""Module for task 0"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """this is the method"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        