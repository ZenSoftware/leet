from random_flip_matrix import Solution


def test1():
    obj = Solution(3, 2)
    param1 = obj.flip()
    assert obj.matrix[param1[0]][param1[1]] == 1
