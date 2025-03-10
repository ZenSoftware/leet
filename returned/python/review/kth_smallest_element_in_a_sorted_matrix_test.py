from kth_smallest_element_in_a_sorted_matrix import Solution

def test1():
    assert Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13

def test2():
    assert Solution().kthSmallest([[-5]], 1) == -5

def test3():
    assert Solution().kthSmallest([[1,2],[1,3]], 1) == 1