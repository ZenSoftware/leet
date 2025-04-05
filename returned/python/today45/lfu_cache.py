# https://leetcode.com/problems/lfu-cache/description/
from collections import defaultdict


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoubleyLinkedList:
    def __init__(self):
        self.left = Node(None)
        self.right = Node(None)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}

    def __len__(self):
        return len(self.map)

    def push_right(self, val):
        node = Node(val, self.right.prev, self.right)
        node.prev.next = node
        node.next.prev = node
        self.map[val] = node

    def pop_left(self):
        res = self.left.next.val
        self.pop(res)
        return res

    def pop(self, val):
        if val in self.map:
            node = self.map.pop(val)
            node.prev.next = node.next
            node.next.prev = node.prev


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 1
        self.val_map = {}
        self.count_map = defaultdict(int)
        self.list_map = defaultdict(DoubleyLinkedList)

    def counter(self, key):
        count = self.count_map[key]
        self.count_map[key] += 1
        self.list_map[count].pop(key)
        self.list_map[count + 1].push_right(key)

        if count == self.lfu_count and len(self.list_map[count]) == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.val_map:
            return -1
        self.counter(key)
        return self.val_map[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.val_map and len(self.val_map) == self.capacity:
            lfu_key = self.list_map[self.lfu_count].pop_left()
            del self.val_map[lfu_key]
            del self.count_map[lfu_key]

        self.val_map[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.count_map[key])
