from third_maximum_number import Solution

def test1():
    assert Solution().thirdMax([3,2,1]) == 1

def test2():
    assert Solution().thirdMax([1,2]) == 2

def test3():
    assert Solution().thirdMax([2,2,3,1]) == 1