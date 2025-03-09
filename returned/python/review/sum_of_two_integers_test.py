from sum_of_two_integers import Solution

def test1():
    assert Solution().getSum(1, 2) == 3

def test2():
    assert Solution().getSum(2, 3) == 5

def test3():
    assert Solution().getSum(-1, 1) == 0