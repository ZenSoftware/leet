from range_sum_query_mutable import NumArray

def test1():
    numArray = NumArray([1, 3, 5])
    assert numArray.sumRange(0, 2) == 9
    numArray.update(1, 2)
    assert numArray.sumRange(0, 2) == 8