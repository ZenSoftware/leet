from typing import List, Optional
from partition_list import Solution, ListNode

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

def test2():
    nodes = to_nodes([1,4,3,2,5,2])
    result = Solution().partition(nodes, 3)
    assert to_array(result) == [1,2,2,4,3,5]

def test3():
    nodes = to_nodes([2,1])
    result = Solution().partition(nodes, 2)
    assert to_array(result) == [1,2]