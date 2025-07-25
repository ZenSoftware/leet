from wiggle_subsequence import Solution

def test1():
    assert Solution().wiggleMaxLength([1,7,4,9,2,5]) == 6
    
def test2():
    assert Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7

def test3():
    assert Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2

def test4():
    assert Solution().wiggleMaxLength([5,5,5,5,5,5,5]) == 1

def test5():
    assert Solution().wiggleMaxLength([34]) == 1
