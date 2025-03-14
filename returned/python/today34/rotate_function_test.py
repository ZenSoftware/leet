from rotate_function import Solution

def test1():
    assert Solution().maxRotateFunction([4,3,2,6]) == 26

def test2():
    assert Solution().maxRotateFunction([100]) == 0