from kth_largest_element_in_an_array_attempt2 import Solution


def test1():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5


def test2():
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
