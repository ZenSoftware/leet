from combination_sum import Solution

def test1():
    assert Solution().combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]

def test2():
    assert Solution().combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]

def test3():
    assert Solution().combinationSum([2], 1) == []