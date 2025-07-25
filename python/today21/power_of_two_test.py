from power_of_two import Solution

def test1():
    assert Solution().isPowerOfTwo(1) == True

def test2():
    assert Solution().isPowerOfTwo(16) == True

def test3():
    assert Solution().isPowerOfTwo(3) == False

def test4():
    assert Solution().isPowerOfTwo(0) == False