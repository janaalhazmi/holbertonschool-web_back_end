#!/usr/bin/env python3
"""this is a module for the 7th task"""
from typing import List, Tuple


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """this is the method"""
    return (k, float(v ** 2))
