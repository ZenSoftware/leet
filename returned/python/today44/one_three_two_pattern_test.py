from one_three_two_pattern import Solution


def test1():
    assert Solution().find132pattern([1, 2, 3, 4]) == False


def test2():
    assert Solution().find132pattern([3, 1, 4, 2]) == True


def test3():
    assert Solution().find132pattern([-1, 3, 2, 0]) == True


def test4():
    assert Solution().find132pattern([4, 3, 2, 1]) == False
