from non_overlapping_intervals import Solution


def test1():
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1


def test2():
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2


def test3():
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0


def test4():
    assert (
        Solution().eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == 2
    )


def test5():
    intervals = [
        [-52, 31],
        [-73, -26],
        [82, 97],
        [-65, -11],
        [-62, -49],
        [95, 99],
        [58, 95],
        [-31, 49],
        [66, 98],
        [-63, 2],
        [30, 47],
        [-40, -26],
    ]
    assert Solution().eraseOverlapIntervals(intervals) == 7


def test6():
    intervals = [[1, 3], [2, 4], [3, 4]]
    assert Solution().eraseOverlapIntervals(intervals) == 1
