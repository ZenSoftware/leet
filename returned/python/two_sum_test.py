import two_sum

def test1():
    result = two_sum.Solution().twoSum([2,7,11,15], 9)
    assert result == [0,1]

def test2():
    result = two_sum.Solution().twoSum([3,2,4], 6)
    assert result == [1,2]

def test3():
    result = two_sum.Solution().twoSum([3,3], 6)
    assert result == [0,1]