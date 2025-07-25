from arithmetic_slices import Solution

def test1():
    assert Solution().numberOfArithmeticSlices([1,2,3,4]) == 3

def test2():
    assert Solution().numberOfArithmeticSlices([1,2,3,4,6,8]) == 4