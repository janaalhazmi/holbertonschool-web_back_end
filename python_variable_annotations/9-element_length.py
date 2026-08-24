#!/usr/bin/env python3
"""this is a module for the last task"""
import typing


def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Calculates the length of each sequence element"""
    return [(i, len(i)) for i in lst]
