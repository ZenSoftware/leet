from valid_perfect_square import Solution

def test1():
    assert Solution().isPerfectSquare(16) == True
    assert Solution().isPerfectSquare(15) == False

def test2():
    for i in range(1000):
        l, r = i, 1000-i
        m1 = (l+r) // 2
        m2 = l + ((r-l) // 2)
        assert m1 == m2