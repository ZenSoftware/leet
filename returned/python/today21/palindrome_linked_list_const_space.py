# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head
        return self.solve(head)

    def solve(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        ans = self.solve(head.next) and self.curr.val == head.val
        self.curr = self.curr.next
        return ans