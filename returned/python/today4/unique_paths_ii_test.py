from unique_paths_ii import Solution

def test1():
    assert Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2

def test2():
    assert Solution().uniquePathsWithObstacles([[0,1],[0,0]]) == 1

def test3():
    assert Solution().uniquePathsWithObstacles([[0,0]]) == 1