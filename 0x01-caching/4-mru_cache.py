#!/usr/bin/python3
""" FIFOCache first im first out """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """First im first out"""

    def put(self, key, item):
        """save item and removes rhe first if full"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        if len(self.cache_data) == self.MAX_ITEMS:
            lock, value = self.cache_data.popitem()
            print("DISCARD: {}".format(lock))
        self.cache_data[key] = item

    def get(self, key):
        """return data matched to key"""
        try:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
        except KeyError:
            pass
        return self.cache_data.get(key)
