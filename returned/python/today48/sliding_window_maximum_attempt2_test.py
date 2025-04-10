from sliding_window_maximum_attempt2 import Solution


def test1():
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]


def test2():
    assert Solution().maxSlidingWindow([1], 1) == [1]
