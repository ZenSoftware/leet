from find_right_interval import Solution


def test1():
    assert Solution().findRightInterval([[1, 2]]) == [-1]


def test2():
    assert Solution().findRightInterval([[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1]


def test3():
    intervals = [[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]
    result = Solution().findRightInterval(intervals)
    assert result == [3, 3, 3, 4, 5, -1]
