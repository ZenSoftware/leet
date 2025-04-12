from combinations_attempt2 import Solution


def test1():
    assert Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


def test2():
    assert Solution().combine(1, 1) == [[1]]
