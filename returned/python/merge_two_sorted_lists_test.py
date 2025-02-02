from merge_two_sorted_lists import Solution, to_array, to_nodes

def test1():
    head = to_nodes([1,2,3,4,5,6])
    assert to_array(head) == [1,2,3,4,5,6]

    head = to_nodes([])
    assert to_array(head) == []

def test2():
    l1 = to_nodes([1,2,4])
    l2 = to_nodes([1,3,4])
    result = Solution().mergeTwoLists(l1, l2)
    assert to_array(result) == [1,1,2,3,4,4]

def test3():
    l1 = to_nodes([])
    l2 = to_nodes([])
    result = Solution().mergeTwoLists(l1, l2)
    assert to_array(result) == []

def test4():
    l1 = to_nodes([])
    l2 = to_nodes([0])
    result = Solution().mergeTwoLists(l1, l2)
    assert to_array(result) == [0]

def test5():
    l1 = to_nodes([1,6])
    l2 = to_nodes([3,4,5])
    result = Solution().mergeTwoLists(l1, l2)
    assert to_array(result) == [1,3,4,5,6]

def test6():
    l1 = to_nodes([1,2,4])
    l2 = to_nodes([1,3,4])
    result = Solution().mergeTwoLists(l1, l2)
    assert to_array(result) == [1,1,2,3,4,4]

def test7():
    l1 = to_nodes([5])
    l2 = to_nodes([1,2,4])
    result = Solution().mergeTwoLists(l1, l2)
    assert to_array(result) == [1,2,4,5]