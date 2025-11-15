from coin_change_ii import Solution


def test1():
    assert Solution().change(5, [1, 2, 5]) == 4


def test2():
    assert Solution().change(3, [2]) == 0


def test3():
    assert Solution().change(10, [10]) == 1
