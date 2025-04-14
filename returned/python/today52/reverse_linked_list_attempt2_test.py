from typing import List, Optional
from reverse_linked_list_attempt2 import ListNode, Solution


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


def test_healpers():
    nodes = to_nodes([1, 2, 3, 4, 5])
    assert to_array(nodes) == [1, 2, 3, 4, 5]

    nodes = to_nodes([])
    assert to_array(nodes) == []


def test1():
    nodes = to_nodes([1, 2, 3, 4, 5])
    result = Solution().reverseList(nodes)
    assert to_array(result) == [5, 4, 3, 2, 1]


def test2():
    nodes = to_nodes([1, 2])
    result = Solution().reverseList(nodes)
    assert to_array(result) == [2, 1]


def test3():
    nodes = to_nodes([])
    result = Solution().reverseList(nodes)
    assert to_array(result) == []
