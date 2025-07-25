from typing import Dict, Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        nodes: Dict[Node, Node] = {}
        pointer = head

        while pointer:
            nodes[pointer] = Node(pointer.val)
            pointer = pointer.next

        for n in nodes:
            copy = nodes[n]
            if n.next:
                copy.next = nodes[n.next]
            if n.random:
                copy.random = nodes[n.random]

        return nodes[head]
