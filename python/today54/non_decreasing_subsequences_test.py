from non_decreasing_subsequences import Solution


def test1():
    assert Solution().findSubsequences([4, 6, 7, 7]) == [
        [7, 7],
        [4, 6],
        [4, 7, 7],
        [6, 7],
        [6, 7, 7],
        [4, 6, 7],
        [4, 6, 7, 7],
        [4, 7],
    ]


def test2():
    assert Solution().findSubsequences([4, 4, 3, 2, 1]) == [[4, 4]]
