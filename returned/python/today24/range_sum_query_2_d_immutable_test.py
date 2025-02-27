from range_sum_query_2_d_immutable import NumMatrix

def test1():
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    assert numMatrix.sumRegion(2, 1, 4, 3) == 8  # return 8 (i.e sum of the red rectangle)
    assert numMatrix.sumRegion(1, 1, 2, 2) == 11 # return 11 (i.e sum of the green rectangle)
    assert numMatrix.sumRegion(1, 2, 2, 4) == 12 # return 12 (i.e sum of the blue rectangle)