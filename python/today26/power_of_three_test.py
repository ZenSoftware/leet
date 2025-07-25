from power_of_three import Solution

def test1():
    assert Solution().isPowerOfThree(27) == True

def test2():
    assert Solution().isPowerOfThree(0) == False

def test3():
    assert Solution().isPowerOfThree(-1) == False

def test4():
    assert Solution().isPowerOfThree(1) == True

def test5():
    assert Solution().isPowerOfThree(243) == True

def test6():
    assert Solution().isPowerOfThree(45) == False