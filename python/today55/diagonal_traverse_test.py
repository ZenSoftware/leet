from diagonal_traverse import Solution


def test1():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().findDiagonalOrder(mat) == [1, 2, 4, 7, 5, 3, 6, 8, 9]


def test2():
    mat = [[1, 2], [3, 4]]
    assert Solution().findDiagonalOrder(mat) == [1, 2, 3, 4]
