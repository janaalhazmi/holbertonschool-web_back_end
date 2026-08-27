#!/usr/bin/env python3
"""this is the module for the 3rd task"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """this is the method"""
    return asyncio.create_task(wait_random(max_delay))
