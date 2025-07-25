from counting_bits_attempt2 import Solution


def test1():
    assert Solution().countBits(2) == [0, 1, 1]


def test2():
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
