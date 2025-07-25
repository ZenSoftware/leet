from target_sum import Solution

def test1():
    assert Solution().findTargetSumWays([1,1,1,1,1], 3) == 5

def test2():
    assert Solution().findTargetSumWays([1], 1) == 1