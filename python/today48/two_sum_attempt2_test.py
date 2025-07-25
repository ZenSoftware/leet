from two_sum_attempt2 import Solution


def test1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test2():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test3():
    assert Solution().twoSum([3, 3], 6) == [0, 1]
