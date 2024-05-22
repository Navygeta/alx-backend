#!/usr/bin/env python3

'''FIFO caching
'''

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and is a caching system.
    '''

    def __init__(self):
        '''Initialize the FIFO cache with an ordered dictionary.'''
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

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the first item (oldest) from the cache
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        # Add the new item to the cache
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
