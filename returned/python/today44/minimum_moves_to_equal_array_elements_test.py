from minimum_moves_to_equal_array_elements import Solution


def test1():
    assert Solution().minMoves([1, 2, 3]) == 3


def test2():
    assert Solution().minMoves([1, 1, 1]) == 0
