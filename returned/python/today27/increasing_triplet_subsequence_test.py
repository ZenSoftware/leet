from increasing_triplet_subsequence import Solution

def test1():
    assert Solution().increasingTriplet([1,2,3,4,5]) == True

def test2():
    assert Solution().increasingTriplet([5,4,3,2,1]) == False

def test3():
    assert Solution().increasingTriplet([2,1,5,0,4,6]) == True