from next_greater_element_ii import Solution


def test1():
    assert Solution().nextGreaterElements([1, 2, 1]) == [2, -1, 2]


def test2():
    assert Solution().nextGreaterElements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
