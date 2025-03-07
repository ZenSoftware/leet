from remove_nth_node_from_end_of_list import Solution, to_array, to_nodes

def test1():
    nodes = to_nodes([1,2,3,4,5])
    assert to_array(nodes) == [1,2,3,4,5]

def test2():
    head = to_nodes([1,2,3,4,5])
    result = Solution().removeNthFromEnd(head, 2)
    assert to_array(result) == [1,2,3,5]

def test3():
    head = to_nodes([1])
    result = Solution().removeNthFromEnd(head, 1)
    assert to_array(result) == []

def test4():
    head = to_nodes([1,2])
    result = Solution().removeNthFromEnd(head, 1)
    assert to_array(result) == [1]