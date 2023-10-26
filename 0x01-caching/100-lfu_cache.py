#!/usr/bin/python3
""" Less Frequent purge """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Less Frequent used cache"""

    def put(self, key, item):
        """updates cache divtiomary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            count = self.get_freq(key)
            self.cache_data[key] = [item, count]
            self.update_freq(key)
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            maxim = 1000
            for lock in self.cache_data:
                if self.get_freq(lock) < maxim:
                    maxim, ky = self.get_freq(lock), lock
            self.cache_data.pop(ky)
            print("DISCARD: {}".format(ky))
        self.cache_data[key] = [item, 0]

    def update_freq(self, key):
        """updates the freq of a key"""
        if key in self.cache_data:
            count = self.cache_data.get(key)
            self.cache_data.pop(key)
            self.cache_data[key] = [count[0], count[1] + 1]

    def get_freq(self, key):
        """returns freq of usef key"""
        if key in self.cache_data:
            return self.cache_data[key][1]
        return

    def get(self, key):
        """returns data associated"""
        if key is None or key not in self.cache_data:
            return
        self.update_freq(key)
        return self.cache_data[key][0]

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            try:
                print("{}: {}".format(key, self.cache_data.get(key)[0]))
            except IndexError:
                print("{}: {}".format(key, self.cache_data.get(key)))
