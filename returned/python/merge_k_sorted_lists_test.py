from merge_k_sorted_lists import Solution, to_array, to_nodes, to_node_list

def test1():
    nodes = to_nodes([1,2,3,4,5])
    assert to_array(nodes) == [1,2,3,4,5]

# def test2():
#     lists = to_node_list([[1,4,5],[1,3,4],[2,6]])
#     result = Solution.mergeKLists(None, lists)
#     assert to_array(result) == [1,1,2,3,4,4,5,6]
    
# def test3():
#     lists = to_node_list([])
#     result = Solution.mergeKLists(None, lists)
#     assert to_array(result) == []

# def test4():
#     lists = to_node_list([[]])
#     result = Solution.mergeKLists(None, lists)
#     assert to_array(result) == []

