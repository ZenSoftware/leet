from two_sum_ii_input_array_is_sorted import Solution

def test1():
    assert Solution.twoSum(None, [2,7,11,15], 9) == [1,2]

def test2():
    assert Solution.twoSum(None, [2,3,4], 6) == [1,3]

def test3():
    assert Solution.twoSum(None, [-1,0], -1) == [1,2]