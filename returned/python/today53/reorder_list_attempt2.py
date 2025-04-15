# https://leetcode.com/problems/reorder-list/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        pointer = head
        while pointer:
            nodes.append(pointer)
            pointer = pointer.next

        dummy = ListNode()
        pointer = dummy
        is_left = True
        left, right = 0, len(nodes) - 1
        while left <= right:
            if is_left:
                pointer.next = nodes[left]
                left += 1
            else:
                pointer.next = nodes[right]
                right -= 1
            pointer = pointer.next
            is_left = not is_left
        pointer.next = None
        return dummy.next
