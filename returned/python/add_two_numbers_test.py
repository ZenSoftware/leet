from add_two_numbers import Solution, to_nodes, to_array

def test1():
    l1 = to_nodes([1,2,3,4])
    assert to_array(l1) == [1,2,3,4]

def test2():
    l1 = to_nodes([2,4,3])
    l2 = to_nodes([5,6,4])
    result = Solution().addTwoNumbers(l1, l2)
    assert to_array(result) == [7,0,8]

def test3():
    l1 = to_nodes([0])
    l2 = to_nodes([0])
    result = Solution().addTwoNumbers(l1, l2)
    assert to_array(result) == [0]

def test4():
    l1 = to_nodes([9,9,9,9,9,9,9])
    l2 = to_nodes([9,9,9,9])
    result = Solution().addTwoNumbers(l1, l2)
    assert to_array(result) == [8,9,9,9,0,0,0,1]
