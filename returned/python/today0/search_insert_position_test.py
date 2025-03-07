from search_insert_position import Solution

def test1():
    assert Solution().searchInsert([1,3,5,6], 5) == 2

def test2():
    assert Solution().searchInsert([1,3,5,6], 2) == 1
    
def test3():
    assert Solution().searchInsert([1,3,5,6], 7) == 4
    
def test4():
    assert Solution().searchInsert([1], 1) == 0

def test5():
    assert Solution().searchInsert([1,3], 2) == 1
