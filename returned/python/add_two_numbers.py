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
        dummy_result_head = ListNode()
        pointer = dummy_result_head
        carry = 0

        while (l1 != None) | (l2 != None):
            if l1 == None:
                sum = l2.val + carry
                l2 = l2.next
            elif l2 == None:
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
                
            if sum >= 10:
                sum -= 10
                carry = 1
            else:
                carry = 0

            pointer.next = ListNode(sum)
            pointer = pointer.next
            

        if carry == 1:
            pointer.next = ListNode(1)
            
        return dummy_result_head.next