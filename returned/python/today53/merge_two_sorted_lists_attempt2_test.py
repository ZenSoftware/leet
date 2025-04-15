from typing import List, Optional
from merge_two_sorted_lists_attempt2 import ListNode, Solution


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
    list1 = to_nodes([1, 2, 4])
    list2 = to_nodes([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_array(result) == [1, 1, 2, 3, 4, 4]


def test2():
    list1 = to_nodes([])
    list2 = to_nodes([])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_array(result) == []


def test3():
    list1 = to_nodes([])
    list2 = to_nodes([0])
    result = Solution().mergeTwoLists(list1, list2)
    assert to_array(result) == [0]
