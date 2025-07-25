# https://leetcode.com/problems/lru-cache/

from typing import Dict, List, Optional

class Node:
    def __init__(self, key = None, value = None, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash: Dict[int,Node] = {}

        self.head = Node('HEAD')
        self.tail = Node('TAIL')
        self.head.prev = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.move_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.move_to_tail(node)
        else:
            if self.size < self.capacity:
                self.size += 1
            else:
                self.hash.pop(self.head.prev.key)
                new_head_prev = self.head.prev.prev
                self.head.prev = new_head_prev
                new_head_prev.next = self.head

            node = Node(key, value)
            self.hash[key] = node
            node.prev = self.tail
            node.next = self.tail.next
            self.tail.next.prev = node
            self.tail.next = node

    def move_to_tail(self, node: Node):
        if node.prev != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            node.next = self.tail.next
            self.tail.next.prev = node
            self.tail.next = node

def to_array_forward(head: Optional[Node]) -> List[int]:
    if not head:
        return []
    result = []
    while head:
        result.append(head.key)
        head = head.next
    return result

def to_array_reverse(tail: Optional[Node]) -> List[int]:
    if not tail:
        return []
    result = []
    while tail:
        result.append(tail.key)
        tail = tail.prev
    return result