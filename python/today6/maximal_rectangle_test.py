from maximal_rectangle import Solution

def test1():
    input = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert Solution().maximalRectangle(input) == 6

def test2():
    input = [["0"]]
    assert Solution().maximalRectangle(input) == 0

def test3():
    input = [["1"]]
    assert Solution().maximalRectangle(input) == 1