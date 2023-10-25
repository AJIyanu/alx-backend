#!/usr/bin/python3
""" FIFOCache first im first out """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """First im first out"""

    def put(self, key, item):
        """save item and removes rhe first if full"""
        if key is None or item is None:
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            lock, value = self.cache_data.popitem()
            print("DISCARD: {}".format(lock))
        self.cache_data[key] = item

    def get(self, key):
        """return data matched to key"""
        return self.cache_data.get(key)
