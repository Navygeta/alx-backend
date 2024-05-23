#!/usr/bin/env python3
"""MRU Caching.

Implements a Most Recently Used (MRU) caching strategy.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class implementing Most Recently Used (MRU) caching.

    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If the cache is at its maximum capacity, it discards the
        least recently used item.

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key if it exists in the cache,
            otherwise returns None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
