from triangle import Solution

def test1():
    assert Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11

def test2():
    assert Solution().minimumTotal([[-10]]) == -10
