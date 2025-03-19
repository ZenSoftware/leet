from typing import List, Optional
from flatten_a_multilevel_doubly_linked_list import Solution, Node

def to_nodes(elements: List[int]) -> Optional[Node]:
    if not elements:
        return None
    prev = None
    for e in reversed(elements):
        node = Node(e, None, None, None)
        node.next = prev
        if prev:
            prev.prev = node
        prev = node
    return prev

def to_array(head: Optional[Node]) -> List[int]:
    if not head:
        return []
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def to_array_reverse(head: Optional[Node]) -> List[int]:
    if not head:
        return []
    pointer = head
    while pointer.next:
        pointer = pointer.next
    result = []
    while pointer:
        result.append(pointer.val)
        pointer = pointer.prev
    return result

def test_conversions():
    nodes = to_nodes([1,2,3,4,5])
    assert to_array(nodes) == [1,2,3,4,5]
    assert to_array_reverse(nodes) == [5,4,3,2,1]

def test1():
    n1 = Node(1, None, None, None)
    n2 = Node(2, None, None, None)
    n3 = Node(3, None, None, None)
    n4 = Node(4, None, None, None)
    n5 = Node(5, None, None, None)
    n6 = Node(6, None, None, None)
    n7 = Node(7, None, None, None)
    n8 = Node(8, None, None, None)
    n9 = Node(9, None, None, None)
    n10 = Node(10, None, None, None)
    n11 = Node(11, None, None, None)
    n12 = Node(12, None, None, None)
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    n4.next = n5
    n5.prev = n4
    n5.next = n6
    n6.prev = n5
    n3.child = n7
    n7.next = n8
    n8.prev = n7
    n8.next = n9
    n9.prev = n8
    n9.next = n10
    n10.prev = n9
    n8.child = n11
    n11.next = n12
    n12.prev = n11
    '''
    1-2-3-4-5-6
        |
        7-8-9-10
          |
          11-12
    '''
    result = Solution().flatten(n1)
    assert to_array(result) == [1,2,3,7,8,11,12,9,10,4,5,6]
    assert to_array_reverse(result) == [6,5,4,10,9,12,11,8,7,3,2,1]
    assert n1.prev == None and n6.next == None
    pointer = result
    while pointer:
        assert pointer.child == None
        pointer = pointer.next

def test2():
    n1 = Node(1, None, None, None)
    n2 = Node(2, None, None, None)
    n3 = Node(3, None, None, None)
    n1.child = n2
    n2.child = n3
    result = Solution().flatten(n1)
    assert to_array(result) == [1,2,3]
    assert to_array_reverse(result) == [3,2,1]