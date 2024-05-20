#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._dataset = None
        self._indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self._dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self._dataset = dataset[1:]

        return self._dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self._indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self._indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self._indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve information about a page from a given index and with a
           specified size."""
        data = self.indexed_dataset()
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
