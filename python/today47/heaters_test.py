from heaters import Solution


def test1():
    assert Solution().findRadius([1, 2, 3], [2]) == 1


def test2():
    assert Solution().findRadius([1, 2, 3, 4], [1, 4]) == 1


def test3():
    assert Solution().findRadius([1, 5], [2]) == 3
