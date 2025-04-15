from typing import List, Optional
from merge_k_sorted_lists_attempt2 import ListNode, Solution


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
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for a in arrays:
        lists.append(to_nodes(a))

    result = Solution().mergeKLists(lists)
    assert to_array(result) == [1, 1, 2, 3, 4, 4, 5, 6]


def test2():
    assert Solution().mergeKLists([]) == None


def test3():
    assert Solution().mergeKLists([[]]) == None
