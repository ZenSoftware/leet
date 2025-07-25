from remove_duplicates_from_sorted_list_ii import Solution, to_array, to_nodes

def test1():
    head = to_nodes([1,2,3,4,5])
    assert to_array(head) == [1,2,3,4,5]

def test2():
    input = to_nodes([1,2,3,3,4,4,5])
    result = Solution().deleteDuplicates(input)
    assert to_array(result) == [1,2,5]

def test3():
    input = to_nodes([1,1,1,2,3])
    result = Solution().deleteDuplicates(input)
    assert to_array(result) == [2,3]

def test4():
    input = to_nodes([1,1])
    result = Solution().deleteDuplicates(input)
    assert to_array(result) == []