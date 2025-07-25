# https://leetcode.com/problems/lru-cache/description/


class Node:
    def __init__(self, key: int, value: int, prev: "Node" = None, next: "Node" = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    """
    Space: O(n)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash: dict[int, Node] = {}
        self.head = Node("HEAD", None)
        self.tail = Node("TAIL", None)
        self.tail.next = self.head
        self.head.prev = self.tail

    def move_to_front(self, node: Node):
        if self.head.prev == node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head.prev
        node.next = self.head
        node.prev.next = node
        node.next.prev = node

    # Time: O(1)
    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.move_to_front(node)
        return node.value

    # Time: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.move_to_front(node)
            return
        if self.size >= self.capacity:
            evict = self.tail.next
            self.tail.next = evict.next
            evict.next.prev = evict.prev
            del self.hash[evict.key]
            self.size -= 1
        node = Node(key, value, self.head.prev, self.head)
        node.prev.next = node
        node.next.prev = node
        self.hash[key] = node
        self.size += 1
