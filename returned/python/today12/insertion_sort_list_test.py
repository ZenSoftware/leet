from typing import List, Optional
from insertion_sort_list import ListNode, Solution

def to_nodes(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    prev = None
    for e in reversed(elements):
        node = ListNode(e)
        node.next = prev
        prev = node
    return prev

def to_array(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test1():
    nodes = to_nodes([1,2,3,4,5])
    assert to_array(nodes) == [1,2,3,4,5]
    
    nodes = to_nodes([])
    assert to_array(nodes) == []

def test2():
    input = to_nodes([4,2,1,3])
    result = Solution().insertionSortList(input)
    assert to_array(result) == [1,2,3,4]
    
def test3():
    input = to_nodes([-1,5,3,4,0])
    result = Solution().insertionSortList(input)
    assert to_array(result) == [-1,0,3,4,5]
