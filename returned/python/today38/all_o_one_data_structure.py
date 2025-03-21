# https://leetcode.com/problems/all-oone-data-structure/
from typing import Dict, List


class Node:
    def __init__(self):
        self.count = 1
        self.min_index = None
        self.max_index = None


class AllOne:
    def __init__(self):
        self.min_heap = MinHeap(key=lambda x: x.count)
        self.max_heap = MaxHeap(key=lambda x: x.count)
        self.nodes: Dict[str, Node] = {}

    def inc(self, key: str) -> None:
        pass

    def dec(self, key: str) -> None:
        pass

    def getMaxKey(self) -> str:
        pass

    def getMinKey(self) -> str:
        pass
