from max_consecutive_ones import Solution


def test1():
    assert Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3


def test2():
    assert Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
