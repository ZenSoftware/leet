from self_crossing import Solution

def test1():
    assert Solution().isSelfCrossing([2,1,1,2]) == True

def test2():
    assert Solution().isSelfCrossing([1,2,3,4]) == False

def test3():
    assert Solution().isSelfCrossing([1,1,1,2,1]) == True

def test4():
    assert Solution().isSelfCrossing([1,1,1,1]) == True

def test5():
    assert Solution().isSelfCrossing([1,1,2,1,1]) == True

def test6():
    assert Solution().isSelfCrossing([3,3,3,2,1,1]) == False
