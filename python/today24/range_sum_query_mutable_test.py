from range_sum_query_mutable import NumArray, BinaryIndexTree

def test_bit():
    bit = BinaryIndexTree([1,2,3,4,5])
    assert bit.get_sum(0) == 1
    assert bit.get_sum(1) == 3
    assert bit.get_sum(2) == 6
    assert bit.get_sum(3) == 10
    assert bit.get_sum(4) == 15

    bit.update(0,1)
    assert bit.get_sum(0) == 2
    assert bit.get_sum(1) == 4
    assert bit.get_sum(2) == 7
    assert bit.get_sum(3) == 11
    assert bit.get_sum(4) == 16

def test1():
    numArray = NumArray([1, 3, 5])
    assert numArray.sumRange(0, 2) == 9
    numArray.update(1, 2)
    assert numArray.sumRange(0, 2) == 8