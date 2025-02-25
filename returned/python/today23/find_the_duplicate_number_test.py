from find_the_duplicate_number import Solution

def test1():
    assert Solution().findDuplicate([1,3,4,2,2]) == 2
    
def test2():
    assert Solution().findDuplicate([3,1,3,4,2]) == 3

def test3():
    assert Solution().findDuplicate([3,3,3,3,3]) == 3
