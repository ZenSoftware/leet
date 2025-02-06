from sort_colors import Solution

def test1():
    input = [2,0,2,1,1,0]
    Solution().sortColors(input)
    assert input == [0,0,1,1,2,2]

def test2():
    input = [2,0,1]
    Solution().sortColors(input)
    assert input == [0,1,2]

def test3():
    input = [1,2,2,1,2,0]
    Solution().sortColors(input)
    assert input == [0,1,1,2,2,2]