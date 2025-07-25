from kth_smallest_element_in_a_sorted_matrix_attempt2 import Solution


def test1():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    assert Solution().kthSmallest(matrix, 8) == 13


def test2():
    matrix = [[-5]]
    assert Solution().kthSmallest(matrix, 1) == -5


def test3():
    matrix = [[1, 2], [1, 3]]
    assert Solution().kthSmallest(matrix, 2) == 1
