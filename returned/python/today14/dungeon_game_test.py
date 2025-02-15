from dungeon_game import Solution

def test1():
    assert Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7

def test2():
    assert Solution().calculateMinimumHP([[0]]) == 1