from move_zeroes import Solution

def test1():
    input = [0,1,0,3,12]
    Solution().moveZeroes(input)
    assert input == [1,3,12,0,0]

def test2():
    input = [0]
    Solution().moveZeroes(input)
    assert input == [0]