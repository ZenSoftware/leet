from elimination_game import Solution

def test1():
    assert Solution().lastRemaining(9) == 6
    
def test2():
    assert Solution().lastRemaining(1) == 1
    
def test3():
    assert Solution().lastRemaining(500) == 246
    