from remove_duplicates_from_sorted_list import Solution, to_array, to_nodes

def test1():
    nodes = to_nodes([1,2,3,4,5])
    assert to_array(nodes) == [1,2,3,4,5]

def test2():
    nodes = to_nodes([1,1,2])
    result = Solution().deleteDuplicates(nodes) 
    assert to_array(result) == [1,2]

def test3():
    nodes = to_nodes([1,1,2,3,3])
    result = Solution().deleteDuplicates(nodes) 
    assert to_array(result) == [1,2,3]

def test4():
    nodes = to_nodes([1,1,2])
    result = Solution().deleteDuplicates(nodes) 
    assert to_array(result) == [1,2]

def test5():
    nodes = to_nodes([0,0,0])
    result = Solution().deleteDuplicates(nodes) 
    assert to_array(result) == [0]