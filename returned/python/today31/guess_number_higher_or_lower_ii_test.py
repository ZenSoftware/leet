from guess_number_higher_or_lower_ii import Solution

def test1():
    assert Solution().getMoneyAmount(10) == 16

def test2():
    assert Solution().getMoneyAmount(1) == 0

def test3():
    assert Solution().getMoneyAmount(2) == 1