# https://leetcode.com/problems/linked-list-random-node/description/
from typing import Optional
from random import randint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self) -> int:
        count = 0
        rand = randint(0, self.length-1)
        head = self.head
        while count < rand:
            head = head.next
            count += 1
        return head.val