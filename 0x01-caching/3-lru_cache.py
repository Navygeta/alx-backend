#!/usr/bin/env python3
'''LRU Caching'''

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''A class for implementing an LRU (Least Recently Used) caching system.

    Inherits from BaseCaching and implements caching functionality
    based on the Least Recently Used policy.
    '''

    def __init__(self):
        '''Initializes the LRU cache.'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item to the cache.

        If the key or item is None, the method does nothing.
        If the cache is full, the least recently used item is removed
        before adding the new item.

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
                # Remove the least recently used item (LRU)
                lru_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", lru_key)

            # Add the new item to the cache and move it to the beginning
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            # Update the existing item and move it to the beginning
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        '''Retrieves an item from the cache.

        If the item exists in the cache, it's moved to the beginning
        to signify it's the most recently used.

        Args:
            key: A hashable object representing the key of the item to be
                 retrieved.

        Returns:
            The item associated with the provided key if found, else None.
        '''
        if key is not None and key in self.cache_data:
            # Move item to the beginning to signify it's the most recently used
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
