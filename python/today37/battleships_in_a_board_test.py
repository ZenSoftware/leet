from battleships_in_a_board import Solution

def test1():
    input = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    assert Solution().countBattleships(input) == 2

def test2():
    input = [["."]]
    assert Solution().countBattleships(input) == 0