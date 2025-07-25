from integer_replacement import Solution

def test1():
    assert Solution().integerReplacement(8) == 3

def test2():
    assert Solution().integerReplacement(7) == 4

def test3():
    assert Solution().integerReplacement(4) == 2

def test4():
    assert Solution().integerReplacement(65535) == 17