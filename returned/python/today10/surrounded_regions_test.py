from surrounded_regions import Solution

def test1():
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(board)
    assert board == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]