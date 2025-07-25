from additive_number import Solution

def test1():
    assert Solution().isAdditiveNumber('112358') == True

def test2():
    assert Solution().isAdditiveNumber('199100199') == True

def test3():
    assert Solution().isAdditiveNumber('100011001') == True

def test4():
    assert Solution().isAdditiveNumber('123') == True