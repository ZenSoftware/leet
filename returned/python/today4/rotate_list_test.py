from typing import List, Optional
from rotate_list import Solution, ListNode, to_array, to_nodes

def test1():
    nodes = to_nodes([1,2,3,4,5])
    assert to_array(nodes) == [1,2,3,4,5]

def test2():
    input = to_nodes([1,2,3,4,5])
    result = Solution().rotateRight(input, 77)
    assert to_array(result) == [4,5,1,2,3]
    
def test3():
    input = to_nodes([0,1,2])
    result = Solution().rotateRight(input, 4)
    assert to_array(result) == [2,0,1]
