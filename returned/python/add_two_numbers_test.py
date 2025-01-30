from add_two_numbers import Solution, to_nodes, to_array

def test1():
    l1 = to_nodes([1,2,3,4])
    assert to_array(l1) == [1,2,3,4]

def test2():
    l1 = to_nodes([2,4,3])
    l2 = to_nodes([5,6,4])
    result = Solution.addTwoNumbers(None, l1, l2)
    assert to_array(result) == [7,0,8]