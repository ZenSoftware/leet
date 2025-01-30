from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def to_nodes(array: List[int]) -> Optional[ListNode]:
    if len(array) == 0:
        return None
    prev = None
    for el in reversed(array):
        next = ListNode(el, prev)
        prev = next
    return prev

def to_array(head: Optional[ListNode]) -> List[int]:
    if head == None:
        return []
    result = []
    while head != None:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return None
