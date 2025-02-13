from lru_cache import LRUCache

def test1():
    cache = LRUCache(2)
    cache.put(1, 1)             # cache is {1=1}
    cache.put(2, 2)             # cache is {1=1, 2=2}
    assert cache.get(1) == 1    # return 1
    cache.put(3, 3)             # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert cache.get(2) == -1   # returns -1 (not found)
    cache.put(4, 4)             # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert cache.get(1) == -1   # return -1 (not found)
    assert cache.get(3) == 3    # return 3
    assert cache.get(4) == 4    # return 4
