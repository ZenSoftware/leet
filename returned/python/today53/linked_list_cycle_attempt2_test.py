from typing import List, Optional
from linked_list_cycle_attempt2 import ListNode, Solution


def to_nodes(elements: List[int], pos: int) -> Optional[ListNode]:
    if not elements:
        return None
    prev = None
    nodes = []
    for e in reversed(elements):
        node = ListNode(e)
        nodes.append(node)
        node.next = prev
        prev = node
    if pos != -1:
        nodes[0].next = nodes[-pos - 1]
    return prev


def test1():
    head = to_nodes([3, 2, 0, -4], 1)
    assert Solution().hasCycle(head) == True


def test2():
    head = to_nodes([1, 2], 0)
    assert Solution().hasCycle(head) == True


def test3():
    head = to_nodes([1], -1)
    assert Solution().hasCycle(head) == False
