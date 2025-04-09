from sliding_window_median import Solution


def test1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    result = Solution().medianSlidingWindow(nums, 3)
    assert result == [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]


def test2():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    result = Solution().medianSlidingWindow(nums, 3)
    assert result == [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
