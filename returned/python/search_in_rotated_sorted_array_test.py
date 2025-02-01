from search_in_rotated_sorted_array import Solution

def test1():
    assert Solution.search(None, [4,5,6,7,0,1,2], 0) == 4

def test2():
    assert Solution.search(None, [4,5,6,7,0,1,2], 3) == -1

def test3():
    assert Solution.search(None, [1], 0) == -1