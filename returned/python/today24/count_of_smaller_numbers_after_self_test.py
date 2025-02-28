from bisect import bisect_left, bisect_right
from count_of_smaller_numbers_after_self import Solution

def test1():
    assert Solution().countSmaller([5,2,6,1]) == [2,1,1,0]

def test2():
    assert Solution().countSmaller([-1]) == [0]

def test3():
    assert Solution().countSmaller([-1,-1]) == [0,0]

def test3():
    assert Solution().countSmaller([-1,-1]) == [0,0]

def test_binary_search():
    assert Solution().binarySearch([0,1,2], 3) == 3
    assert bisect_left([0,1,2], 3) == 3
    assert bisect_right([0,1,2], 3) == 3

    assert Solution().binarySearch([0,1,2], 2) == 2
    assert bisect_left([0,1,2], 2) == 2
    assert bisect_right([0,1,2], 2) == 3

    assert Solution().binarySearch([0,1,2], -1) == 0
    assert bisect_left([0,1,2], -1) == 0

    assert Solution().binarySearch([0,1,2,4], 3) == 3
    assert bisect_left([0,1,2,4], 3) == 3
    assert bisect_right([0,1,2,4], 3) == 3

    assert Solution().binarySearch([], 9) == 0
    assert bisect_left([], 9) == 0

    assert Solution().binarySearch([-1,-1], -1) == 0
    assert Solution().binarySearch([-1,-1,-1], -1) == 0

    assert bisect_right([-1,-1,-1], -1) == 3
    assert bisect_left([-1,-1,-1], -1) == 0
