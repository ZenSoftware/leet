from first_missing_positive_attempt2 import Solution


def test1():
    assert Solution().firstMissingPositive([1, 2, 0]) == 3


def test2():
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2


def test3():
    assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1


def test4():
    assert Solution().firstMissingPositive([1, 1]) == 2
