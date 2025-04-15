# https://leetcode.com/problems/reorder-list/description/
from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = deque()
        pointer = head
        while pointer:
            nodes.append(pointer)
            pointer = pointer.next

        dummy = ListNode()
        pointer = dummy
        is_left = True
        while nodes:
            if is_left:
                node = nodes.popleft()
            else:
                node = nodes.pop()
            pointer.next = node
            pointer = pointer.next
            is_left = not is_left
        pointer.next = None
        return dummy.next
