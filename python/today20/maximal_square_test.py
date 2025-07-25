from maximal_square import Solution

def test1():
    input = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert Solution().maximalSquare(input) == 4

def test2():
    input = [["0","1"],["1","0"]]
    assert Solution().maximalSquare(input) == 1