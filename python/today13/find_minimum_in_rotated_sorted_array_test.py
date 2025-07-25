from find_minimum_in_rotated_sorted_array import Solution

def test1():
    assert Solution().findMin([3,4,5,1,2]) == 1

def test2():
    assert Solution().findMin([4,5,6,7,0,1,2]) == 0

def test3():
    assert Solution().findMin([11,13,15,17]) == 11

def test4():
    assert Solution().findMin([3,1,2]) == 1

def test5():
    assert Solution().findMin([3,4,1,2]) == 1

def test6():
    assert Solution().findMin([4,1,2,3]) == 1