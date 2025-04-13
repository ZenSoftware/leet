from search_a_2_d_matrix_attemp2 import Solution


def test1():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert Solution().searchMatrix(matrix, 3) == True


def test2():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert Solution().searchMatrix(matrix, 13) == False


def test3():
    matrix = [[1]]
    assert Solution().searchMatrix(matrix, 2) == False
