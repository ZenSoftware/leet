from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return head
        
        fast = head
        slow = head

        # Split in half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right = slow.next
        slow.next = None

        # Reverse right list
        prev = None
        while right.next:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        right.next = prev

        # Merge two lists
        left = head
        while right:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right