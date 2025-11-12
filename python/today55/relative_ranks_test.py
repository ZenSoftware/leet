from relative_ranks import Solution


def test1():
    assert Solution().findRelativeRanks([5, 4, 3, 2, 1]) == [
        "Gold Medal",
        "Silver Medal",
        "Bronze Medal",
        "4",
        "5",
    ]


def test2():
    assert Solution().findRelativeRanks([10, 3, 8, 9, 4]) == [
        "Gold Medal",
        "5",
        "Bronze Medal",
        "Silver Medal",
        "4",
    ]
