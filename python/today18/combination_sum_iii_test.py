from combination_sum_iii import Solution

def test1():
    assert Solution().combinationSum3(3, 7) == [[1,2,4]]

def test2():
    assert Solution().combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]

def test3():
    assert Solution().combinationSum3(4, 1) == []

