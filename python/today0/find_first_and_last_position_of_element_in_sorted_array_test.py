from find_first_and_last_position_of_element_in_sorted_array import Solution

def test1():
    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4]

def test2():
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1]

def test3():
    assert Solution().searchRange([], 0) == [-1,-1]