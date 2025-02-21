from contains_duplicate_ii import Solution

def test1():
    assert Solution().containsNearbyDuplicate([1,2,3,1], 3) == True

def test2():
    assert Solution().containsNearbyDuplicate([1,0,1,1], 1) == True

def test3():
    assert Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2) == False