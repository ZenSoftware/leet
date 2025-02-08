# https://leetcode.com/problems/reverse-linked-list-ii/description/
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        pointer = dummy
        before_nodes = None        
        nodes: List[ListNode] = []

        count = 0
        while count <= right:
            if count == left - 1:
                before_nodes = pointer
            if count >= left:
                nodes.append(pointer)
            count += 1
            pointer = pointer.next

        after_nodes = nodes[-1].next

        for i in range(len(nodes)-1, 0, -1):
            nodes[i].next = nodes[i-1]
        
        nodes[0].next = after_nodes
        before_nodes.next = nodes[-1]

        return dummy.next