from frog_jump import Solution

def test1():
    assert Solution().canCross([0,1,3,5,6,8,12,17]) == True
    
def test2():
    assert Solution().canCross([0,1,2,3,4,8,9,11]) == False
    
def test3():
    assert Solution().canCross([0,2]) == False
