from loud_and_rich import Solution


def test1():
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    assert Solution().loudAndRich(richer, quiet) == [5, 5, 2, 5, 4, 5, 6, 7]
