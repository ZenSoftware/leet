from next_greater_element_i import Solution


def test1():
    assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]


def test2():
    assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
