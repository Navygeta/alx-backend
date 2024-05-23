#!/usr/bin/env python3
"""LFU Caching

Implements a Least Frequently Used (LFU) caching strategy.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A class implementing Least Frequently Used (LFU) caching.

    Inherits from BaseCaching.
    """

    FREQ_BITS = {}

    def put(self, key, item):
        """Add an item to the cache.

        If the cache is at its maximum capacity, it discards the least
        frequently used item.

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.
        """
        if key is None or item is None:
            pass
        else:
            count = LFUCache.FREQ_BITS.get(key)
            LFUCache.FREQ_BITS[key] = count + 1 if count else 0
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard_keys = sorted(list(LFUCache.FREQ_BITS.items()),
                                      key=lambda v: v[1])[0:2]
                if discard_keys[0][0] == key:
                    discard_key = discard_keys[1][0]
                else:
                    discard_key = discard_keys[0][0]
                del self.cache_data[discard_key]
                del LFUCache.FREQ_BITS[discard_key]
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key if it exists in the cache,
            otherwise returns None.
        """
        if self.cache_data.get(key):
            count = LFUCache.FREQ_BITS[key]
            LFUCache.FREQ_BITS[key] = count + 1

        return self.cache_data.get(key)
