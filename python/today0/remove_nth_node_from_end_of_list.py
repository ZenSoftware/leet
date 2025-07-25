# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_nodes(elements: List[int]) -> Optional[ListNode]:
    if len(elements) == 0:
        return None
    prev = None
    for el in reversed(elements):
        node = ListNode(el)
        node.next = prev
        prev = node
    return prev
    
def to_array(root: Optional[ListNode]) -> List[int]:
    if not root:
        return []
    result = []
    while root:
        result.append(root.val)
        root = root.next
    return result

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        pointer = dummy
        counter = 1
        trail = None
        while pointer.next != None:
            if counter == n:
                trail = dummy
            elif counter > n:
                trail = trail.next
            counter += 1
            pointer = pointer.next
            
        trail.next = trail.next.next

        return dummy.next