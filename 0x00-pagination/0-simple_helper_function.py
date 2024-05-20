#!/usr/bin/env python3

"""
Simple pagination helper function.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range from a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index of the page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
