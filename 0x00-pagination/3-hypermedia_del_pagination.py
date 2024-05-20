#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size."""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self._dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self._dataset = dataset

        return self._dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves information about a page from a given index and with a
           specified size."""
        data = self.dataset()
        max_index = len(data) - 1

        if index is None:
            index = 0
        assert 0 <= index <= max_index, \
            f"Invalid index. Must be between 0 and {max_index}."

        next_index = min(index + page_size, max_index + 1)
        page_data = [data[i] for i in range(index, next_index)]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
