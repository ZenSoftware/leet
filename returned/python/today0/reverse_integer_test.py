from reverse_integer import Solution

def test1():
    assert Solution().reverse(123) == 321

def test2():
    assert Solution().reverse(-123) == -321

def test3():
    assert Solution().reverse(120) == 21