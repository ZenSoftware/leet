from teemo_attacking import Solution


def test1():
    assert Solution().findPoisonedDuration([1, 4], 2) == 4


def test2():
    assert Solution().findPoisonedDuration([1, 2], 2) == 3


def test3():
    assert Solution().findPoisonedDuration([1, 2, 3, 4], 2) == 5
