from range_sum_query_immutable2 import NumArray

def test1():
    numArray = NumArray([-2, 0, 3, -5, 2, -1])  
    assert numArray.sumRange(0, 2) == 1  # return (-2) + 0 + 3 = 1
    assert numArray.sumRange(2, 5) == -1 # return 3 + (-5) + 2 + (-1) = -1
    assert numArray.sumRange(0, 5) == -3 # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


#    [-2, 0, 3, -5, 2, -1]
# [0, -2, -2, 1, -4, -2, -3]