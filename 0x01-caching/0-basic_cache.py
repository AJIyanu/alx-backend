#!/usr/bin/python3
""" contains the first task bascic cache """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This cache system doesn't have limit"""

    def put(self, key, item):
        """assign to the dictionary cache_data the item value for the key"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """returns value associated with the key"""
        return self.cache_data.get(key)
