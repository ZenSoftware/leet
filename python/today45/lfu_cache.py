# https://leetcode.com/problems/lfu-cache/description/
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 1
        self.freq = defaultdict(OrderedDict)
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val, freq = self.cache[key]
        del self.freq[freq][key]
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freq[freq + 1][key] = val
        self.cache[key] = (val, freq + 1)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)
        else:
            if len(self.cache) >= self.capacity:
                evict_key, _ = self.freq[self.min_freq].popitem(last=False)
                del self.cache[evict_key]

            self.freq[1][key] = value
            self.cache[key] = (value, 1)
            self.min_freq = 1
