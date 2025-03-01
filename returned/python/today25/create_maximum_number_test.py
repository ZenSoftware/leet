from create_maximum_number import Solution

def test1():
    assert Solution().maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) == [9,8,6,5,3]

def test2():
    assert Solution().maxNumber([6,7], [6,0,4], 5) == [6,7,6,0,4]

def test3():
    assert Solution().maxNumber([3,9], [8,9], 3) == [9,8,9]

