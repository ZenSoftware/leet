from search_in_rotated_sorted_array_ii import Solution

def test1():
    assert Solution().search([2,5,6,0,0,1,2], 0) == True

def test2():
    assert Solution().search([2,5,6,0,0,1,2], 3) == False

def test3():
    assert Solution().search([1,0,1,1,1], 0) == True

def test4():
    assert Solution().search([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1], 13) == True