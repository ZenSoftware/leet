from remove_nth_node_from_end_of_list_attempt2 import Solution, ListNode
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


def test_helpers():
    nodes = to_nodes([1, 2, 3, 4, 5])
    assert to_array(nodes) == [1, 2, 3, 4, 5]

    nodes = to_nodes([])
    assert to_array(nodes) == []


def test1():
    nodes = to_nodes([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(nodes, 2)
    assert to_array(result) == [1, 2, 3, 5]


def test2():
    nodes = to_nodes([1])
    result = Solution().removeNthFromEnd(nodes, 1)
    assert to_array(result) == []


def test3():
    nodes = to_nodes([1, 2])
    result = Solution().removeNthFromEnd(nodes, 1)
    assert to_array(result) == [1]
