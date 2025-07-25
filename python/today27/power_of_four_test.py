from power_of_four import Solution

def test1():
    assert Solution().isPowerOfFour(16) == True

def test2():
    assert Solution().isPowerOfFour(5) == False

def test3():
    assert Solution().isPowerOfFour(1) == True