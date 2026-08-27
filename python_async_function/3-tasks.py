#!/usr/bin/env python3
"""this is the module for the 3rd task"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """this is the method"""
    last = asyncio.create_task(wait_random(max_delay))
    return last
