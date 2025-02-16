from number_of_1_bits import Solution

def test1():
    assert Solution().hammingWeight(11) == 3

def test2():
    assert Solution().hammingWeight(128) == 1

def test3():
    assert Solution().hammingWeight(2147483645) == 30