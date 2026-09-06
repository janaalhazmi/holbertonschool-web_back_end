#!/usr/bin/env python3
"""modul for simple function"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """this is the method"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
