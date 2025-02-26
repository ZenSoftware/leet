from range_sum_query_immutable import NumArray

def test1():
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    numArray.sumRange(0, 2) # return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5) # return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3