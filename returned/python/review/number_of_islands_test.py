from number_of_islands import Solution

def test1():
    input = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert Solution().numIslands(input) == 1

def test2():
    input = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert Solution().numIslands(input) == 3

def test3():
    input = [["1","0","1","1","0","1","1"]]
    assert Solution().numIslands(input) == 3