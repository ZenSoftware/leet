from count_of_smaller_numbers_after_self import Solution, BinaryIndexTree

def test1():
    assert Solution().countSmaller([5,2,6,1]) == [2,1,1,0]

def test2():
    assert Solution().countSmaller([-1]) == [0]

def test3():
    assert Solution().countSmaller([-1,-1]) == [0,0]

def test3():
    assert Solution().countSmaller([-1,-1]) == [0,0]

def test_bit():
    bit = BinaryIndexTree(4)
    # [1,2,3,4]
    bit.update(0,1)
    bit.update(1,2)
    bit.update(2,3)
    bit.update(3,4)
    # [1,3,6,10]
    assert bit.query(0) == 1
    assert bit.query(1) == 3
    assert bit.query(2) == 6
    assert bit.query(3) == 10
    bit.update(0,1)
    assert bit.query(0) == 2
    assert bit.query(1) == 4
    assert bit.query(2) == 7
    assert bit.query(3) == 11