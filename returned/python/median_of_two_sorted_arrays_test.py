from median_of_two_sorted_arrays import Solution

def test1():
    result = Solution.findMedianSortedArrays(None, [1,3], [2])
    assert result == 2

def test2():
    result = Solution.findMedianSortedArrays(None, [1,2], [3,4])
    assert result == 2.5

def test3():
    result = Solution.findMedianSortedArrays(None, [1,2,3,4,5,6,7,8], [1,2,3,4,5])
    assert result == 4