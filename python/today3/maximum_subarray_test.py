from maximum_subarray import Solution

def test1():
    assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test2():
    assert Solution().maxSubArray([1]) == 1

def test3():
    assert Solution().maxSubArray([5,4,-1,7,8]) == 23