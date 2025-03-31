from typing import List, Optional
from add_two_numbers_ii import ListNode, Solution


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
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def test_converters():
    nodes = to_nodes([1, 2, 3, 4, 5])
    assert to_array(nodes) == [1, 2, 3, 4, 5]

    nodes = to_nodes([])
    assert to_array(nodes) == []


def test1():
    l1 = to_nodes([7, 2, 4, 3])
    l2 = to_nodes([5, 6, 4])
    result = Solution().addTwoNumbers(l1, l2)
    assert to_array(result) == [7, 8, 0, 7]
