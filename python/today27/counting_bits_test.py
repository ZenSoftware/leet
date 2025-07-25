from counting_bits import Solution

def test1():
    assert Solution().countBits(2) == [0,1,1]

def test2():
    assert Solution().countBits(5) == [0,1,1,2,1,2]

def test3():
    assert Solution().countBits(15) == [0,
                                        1,
                                        1,2,
                                        1,2,2,3,
                                        1,2,2,3,2,3,3,4]
def test4():
    assert Solution().countBits(14) == [0,
                                        1,
                                        1,2,
                                        1,2,2,3,
                                        1,2,2,3,2,3,3]
def test5():
    assert Solution().countBits(4) == [0,1,1,2,1]