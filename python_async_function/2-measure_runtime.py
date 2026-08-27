#!/usr/bin/env python3
"""this is the module for task 2"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int, n: int) -> float:
    """this is the method"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
