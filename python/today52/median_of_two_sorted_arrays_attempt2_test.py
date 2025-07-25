from median_of_two_sorted_arrays_attempt2 import Solution


def test1():
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0


def test2():
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
