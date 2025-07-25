from remove_k_digits import Solution

def test1():
    assert Solution().removeKdigits('1432219', 3) == '1219'

def test2():
    assert Solution().removeKdigits('10200', 1) == '200'

def test3():
    assert Solution().removeKdigits('10', 2) == '0'