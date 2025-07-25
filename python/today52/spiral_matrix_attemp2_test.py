from spiral_matrix_attemp2 import Solution


def test1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Solution().spiralOrder(matrix)
    assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = Solution().spiralOrder(matrix)
    assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
