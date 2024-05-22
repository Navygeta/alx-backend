#!/usr/bin/env python3

'''FIFO caching

This script contains the implementation of a FIFO (First-In, First-Out)
caching system.
'''

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class for implementing a FIFO caching system.

    This class inherits from `BaseCaching` and implements caching
    functionality based on the First-In, First-Out principle.
    '''

    def __init__(self):
        '''Initialize a FIFO cache with an ordered dictionary.'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Store an item in the cache.

        Args:
            key: A hashable object representing the key for the item.
            item: The item to be stored in the cache.

        Returns:
            None
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve an item from the cache.

        Args:
            key: A hashable object representing the key of the item to be
                 retrieved.

        Returns:
            The item associated with the provided key if found, else None.
        '''
        return self.cache_data.get(key, None)
