# https://leetcode.com/problems/linked-list-cycle/description/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False

            if slow == fast:
                return True

        return False
