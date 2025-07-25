from set_matrix_zeroes import Solution

def test1():
    input = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(input)
    assert input == [[1,0,1],[0,0,0],[1,0,1]]

def test2():
    input = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(input)
    assert input == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]