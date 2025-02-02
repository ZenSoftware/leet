from three_sum_closest import Solution

def test1():
    assert Solution().threeSumClosest([-1,2,1,-4], 1) == 2

def test2():
    assert Solution().threeSumClosest([0,0,0], 1) == 0