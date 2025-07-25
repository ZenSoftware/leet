from minimum_genetic_mutation import Solution


def test1():
    assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1


def test2():
    assert (
        Solution().minMutation(
            "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        )
        == 2
    )


def test3():
    assert Solution().minMutation("AACCGGTT", "AACCGGTT", ["AACCGGTA"]) == 0
