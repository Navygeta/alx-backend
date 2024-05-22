#!/usr/bin/env python3
'''LIFO Caching.'''

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Represents a caching system with Last-In, First-Out (LIFO) eviction
    policy.

    Inherits from BaseCaching and implements LIFO caching.
    '''

    def __init__(self):
        '''Initializes the LIFO cache.'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item to the cache.

        If the key or item is None, the method does nothing.
        If the cache is full, the last added item is removed (LIFO eviction).

        Args:
            key: A hashable object representing the key for the item.
            item: The item to be stored in the cache.

        Returns:
            None
        '''
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # If cache is full, remove the last added item (LIFO)
                last_key, _ = self.cache_data.popitem(last=True)
                print('DISCARD:', last_key)

        self.cache_data[key] = item
        # Move the newly added item to the end to signify it's the most recent
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''Retrieves an item from the cache.

        Args:
            key: A hashable object representing the key of the item to be
                 retrieved.

        Returns:
            The item associated with the provided key if found, else None.
        '''
        return self.cache_data.get(key, None)
