from search_a_2_d_matrix import Solution

def test1():
    input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert Solution().searchMatrix(input, 3) == True

def test2():
    input = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert Solution().searchMatrix(input, 13) == False