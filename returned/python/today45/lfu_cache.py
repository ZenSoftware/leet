# https://leetcode.com/problems/lfu-cache/description/


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hashmap = {}

        self.head = Node("HEAD", None)
        self.tail = Node("TAIL", None)
        self.tail.next = self.head
        self.head.prev = self.tail

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self._move_to_front(self.hashmap[key])
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self._move_to_front(node)
        else:
            if self.capacity == self.size:
                del self.hashmap[self.tail.next.key]
                self.tail.next.prev = None
                self.tail.next.next = None
                self.tail.next = self.tail.next.next
                self.size -= 1

            node = Node(key, value, self.head.prev, self.head)
            self.hashmap[key] = node
            node.prev.next = node
            node.next.prev = node
            self.size += 1

    def _move_to_front(self, node: Node):
        if node.next != self.head:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
