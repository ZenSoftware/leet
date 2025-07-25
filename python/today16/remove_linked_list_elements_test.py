from remove_linked_list_elements import Solution, ListNode
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
    head = to_nodes([1,2,6,3,4,5,6])
    result = Solution().removeElements(head, 6)
    assert to_array(result) == [1,2,3,4,5]

def test3():
    head = to_nodes([])
    result = Solution().removeElements(head, 1)
    assert to_array(result) == []

def test4():
    head = to_nodes([7,7,7,7])
    result = Solution().removeElements(head, 7)
    assert to_array(result) == []