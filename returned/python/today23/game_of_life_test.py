from game_of_life import Solution

def test1():
    input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution().gameOfLife(input)
    assert input == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

def test2():
    input = [[1,1],[1,0]]
    Solution().gameOfLife(input)
    assert input == [[1,1],[1,1]]