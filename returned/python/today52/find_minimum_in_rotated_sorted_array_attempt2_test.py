from find_minimum_in_rotated_sorted_array_attempt2 import Solution


def test1():
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1


def test2():
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0


def test3():
    assert Solution().findMin([11, 13, 15, 17]) == 11
