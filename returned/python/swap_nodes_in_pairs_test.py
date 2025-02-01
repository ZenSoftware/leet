from swap_nodes_in_pairs import Solution, to_array, to_nodes

def test1():
    input = to_nodes([1,2,3,4])
    result = Solution.swapPairs(None, input)
    assert to_array(result) == [2,1,4,3]