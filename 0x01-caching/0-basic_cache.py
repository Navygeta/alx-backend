#!/usr/bin/env python3

'''Basic dictionary

This script contains the implementation of a basic dictionary caching system.
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class for implementing a basic dictionary caching system.

    This class inherits from `BaseCaching` and implements basic caching
    functionality using a dictionary.
    '''

    def put(self, key, item):
        '''Store an item in the cache.

        Args:
            key: A hashable object representing the key for the item.
            item: The item to be stored in the cache.

        Returns:
            None
        '''
        if key is not None and item is not None:
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
