from odd_even_linked_list import Solution, ListNode
from typing import List, Optional

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
    input = to_nodes([1,2,3,4,5])
    output = Solution().oddEvenList(input)
    assert to_array(output) == [1,3,5,2,4]

def test3():
    input = to_nodes([2,1,3,5,6,4,7])
    output = Solution().oddEvenList(input)
    assert to_array(output) == [2,3,6,7,1,5,4]