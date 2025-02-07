from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_nodes(elements: List[int]):
    if not elements:
        return None
    prev = None
    for e in reversed(elements):
        node = ListNode(e)
        node.next = prev
        prev = node
    return prev

def to_array(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pointer = dummy

        while pointer.next:
            if pointer.next.next and pointer.next.val == pointer.next.next.val:
                dup_pointer = pointer.next.next
                while dup_pointer.next and dup_pointer.val == dup_pointer.next.val:
                    dup_pointer = dup_pointer.next
                pointer.next = dup_pointer.next
            else:
                pointer = pointer.next

        return dummy.next