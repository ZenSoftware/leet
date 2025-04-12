# https://leetcode.com/problems/all-oone-data-structure/description/
from typing import Optional


class Node:
    def __init__(
        self, count: int, prev: Optional["Node"] = None, next: Optional["Node"] = None
    ):
        self.count = count
        self.keys: set[str] = set()
        self.prev = prev
        self.next = next


class AllOne:
    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.head = Node(float("-inf"))
        self.tail = Node(float("inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            node = self.head.next
            if node.count != 1:
                node = Node(1, self.head, self.head.next)
                node.prev.next = node
                node.next.prev = node
        else:
            cur = self.nodes[key]
            if cur.next.count == cur.count + 1:
                node = cur.next
            else:
                node = Node(cur.count + 1, cur, cur.next)
                node.prev.next = node
                node.next.prev = node
            cur.keys.remove(key)
            if not cur.keys:
                cur.prev.next = node
                node.prev = cur.prev
        node.keys.add(key)
        self.nodes[key] = node

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:
            del self.nodes[key]
        else:
            if cur.prev.count == cur.count - 1:
                node = cur.prev
            else:
                node = Node(cur.count - 1, cur.prev, cur)
                node.prev.next = node
                node.next.prev = node
            node.keys.add(key)
            self.nodes[key] = node
        cur.keys.remove(key)
        if not cur.keys:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    def getMaxKey(self) -> str:
        if not self.nodes:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if not self.nodes:
            return ""
        return next(iter(self.head.next.keys))
