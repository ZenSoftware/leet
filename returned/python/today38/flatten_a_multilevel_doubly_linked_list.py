# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
from typing import Optional, Tuple

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def compute_flatten(head: Node) -> Tuple[Node, Node]:
            pointer = head
            tail = head
            
            while pointer:
                if pointer.child:
                    child_head, child_tail = compute_flatten(pointer.child)
                    child_tail.next = pointer.next
                    if pointer.next:
                        pointer.next.prev = child_tail
                    child_head.prev = pointer
                    pointer.next = child_head
                    pointer.child = None
                    pointer = child_tail
                    
                if not pointer.next:
                    tail = pointer
                pointer = pointer.next
            
            return (head, tail)
        
        compute_flatten(head)
        return head