from three_sum import Solution

def test1():
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1, 0, 1], [-1, -1, 2]] 

def test2():
    assert Solution().threeSum([0,1,1]) == []

def test3():
    assert Solution().threeSum([0,0,0]) == [[0,0,0]]