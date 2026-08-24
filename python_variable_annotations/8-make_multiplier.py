#!/usr/bin/env python3
"""this is a module for the 7th task"""
from typing import List, Tuple, Union
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """this is the method"""
    def multiplier_func(n: float) -> float:
        """this is the inner method"""
        return n * multiplier

    return multiplier_func
