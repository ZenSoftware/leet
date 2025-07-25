from plus_one import Solution

def test1():
    assert Solution().plusOne([1,2,3]) == [1,2,4]

def test2():
    assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]

def test3():
    assert Solution().plusOne([9,9,9]) == [1,0,0,0]