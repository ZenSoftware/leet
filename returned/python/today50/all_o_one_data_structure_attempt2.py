# https://leetcode.com/problems/all-oone-data-structure/description/
from typing import Optional


class Node:
    def __init__(
        self, key: str, prev: Optional["Node"] = None, next: Optional["Node"] = None
    ):
        self.key = key
        self.count = 1
        self.prev = prev
        self.next = next


class AllOne:
    def __init__(self):
        self.nodes: dict[str, Node] = {}

        self.tail = Node("Tail")
        self.tail.count = float("-inf")

        self.head = Node("HEAD")
        self.head.count = float("inf")

        self.tail.next = self.head
        self.head.prev = self.tail

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            node = Node(key, self.tail, self.tail.next)
            node.prev.next = node
            node.next.prev = node
            self.nodes[key] = node
        else:
            node = self.nodes[key]
            node.count += 1
            if node.count > node.next.count:
                pointer = node.next
                while pointer:
                    if pointer.count >= node.count:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        node.prev = pointer.prev
                        node.next = pointer
                        pointer.prev.next = node
                        pointer.prev = node
                    pointer = pointer.next

    def dec(self, key: str) -> None:
        node = self.nodes[key]
        if node.count == 1:
            del self.nodes[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node.count -= 1
            if node.prev.count > node.count:
                pointer = node
                while pointer:
                    if pointer.count <= node.count:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        node.prev = pointer
                        node.next = pointer.next
                        node.prev.next = node
                        node.next.prev = node
                    pointer = pointer.prev

    def getMaxKey(self) -> str:
        if not self.nodes:
            return ""
        return self.head.prev.key

    def getMinKey(self) -> str:
        if not self.nodes:
            return ""
        return self.tail.next.key
