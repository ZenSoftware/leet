from lfu_cache import LFUCache


def test1():
    lfu = LFUCache(2)
    lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
    assert lfu.get(1) == 1  # return 1
    # cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3)  # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
    # cache=[3,1], cnt(3)=1, cnt(1)=2
    assert lfu.get(2) == -1  # return -1 (not found)
    assert lfu.get(3) == 3  # return 3
    # cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)  # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
    # cache=[4,3], cnt(4)=1, cnt(3)=2
    assert lfu.get(1) == -1  # return -1 (not found)
    assert lfu.get(3) == 3  # return 3
    # cache=[3,4], cnt(4)=1, cnt(3)=3
    assert lfu.get(4) == 4  # return 4
    # cache=[4,3], cnt(4)=2, cnt(3)=3


def test2():
    """
    ["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
    [   [3],    [2,2],[1,1], [2],  [1],  [2], [3,3],[4,4], [3],  [2],  [1],  [4]]
    [   null,    null, null,  2,    1,    2,   null, null, -1,    2,    1,    4]
    """
    lfu = LFUCache(3)
    lfu.put(2, 2)
    lfu.put(1, 1)
    assert lfu.get(2) == 2
    assert lfu.get(1) == 1
    assert lfu.get(2) == 2
    lfu.put(3, 3)
    lfu.put(4, 4)
    assert lfu.get(3) == -1
    assert lfu.get(2) == 2
    assert lfu.get(1) == 1
    assert lfu.get(4) == 4
