from lru_cache_attempt2 import LRUCache


def test1():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    assert lRUCache.get(1) == 1  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.get(2) == -1  # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert lRUCache.get(1) == -1  # return -1 (not found)
    assert lRUCache.get(3) == 3  # return 3
    assert lRUCache.get(4) == 4  # return 4


def test2():
    # ["LRUCache","get","get","put","get","put","put", "put", "put","get","put"]
    # [[1],        [6],  [8],[12,1], [2],[15,11],[5,2],[1,15],[4,2], [4], [15,15]]
    lRUCache = LRUCache(1)
    assert lRUCache.get(6) == -1
    assert lRUCache.get(8) == -1
    lRUCache.put(12, 1)
    assert lRUCache.get(2) == -1
    lRUCache.put(15, 11)
    lRUCache.put(5, 2)
    lRUCache.put(1, 15)
    lRUCache.put(4, 2)
    assert lRUCache.get(4) == 2
    lRUCache.put(15, 15)
