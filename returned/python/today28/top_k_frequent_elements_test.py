from top_k_frequent_elements import Solution

def test1():
    assert Solution().topKFrequent([1,1,1,2,2,3], 2) == [1,2]

def test2():
    assert Solution().topKFrequent([1], 1) == [1]