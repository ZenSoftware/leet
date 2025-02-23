# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        
        reversed = ListNode(None)
        while slow:
            next = slow.next
            slow.next = reversed.next
            reversed.next = slow
            slow = next
        
        p1, p2 = head, reversed.next
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True