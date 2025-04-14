from typing import List


class MinHeap:
    def __init__(self, elements: List = [], key=None):
        self.heap = elements
        if key is None:
            self.key = lambda x: x
        else:
            self.key = key
        self.heapify()

    def __len__(self):
        return len(self.heap)

    def heapify(self):
        for i in reversed(range(len(self.heap))):
            self.sift_down(i)

    def sift_up(self, i: int):
        while i != 0 and self.val(i) < self.val(p := (i - 1) // 2):
            self.swap(p, i)
            i = p

    def sift_down(self, i: int):
        size = len(self.heap)
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and r < size:
            if self.val(l) < self.val(r) and self.val(i) > self.val(l):
                self.swap(i, l)
                self.sift_down(l)
            elif self.val(l) >= self.val(r) and self.val(i) > self.val(r):
                self.swap(i, r)
                self.sift_down(r)
        elif l < size:
            if self.val(i) > self.val(l):
                self.swap(i, l)
                self.sift_down(l)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def val(self, i: int):
        return self.key(self.heap[i])

    def push(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def peek(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def pop(self):
        if not self.heap:
            return None
        last_index = len(self.heap) - 1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        result = self.heap.pop()
        self.sift_down(0)
        return result


class MaxHeap(MinHeap):
    def sift_up(self, i: int):
        while i != 0 and self.val(i) > self.val(p := (i - 1) // 2):
            self.swap(p, i)
            i = p

    def sift_down(self, i: int):
        size = len(self.heap)
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and r < size:
            if self.val(l) > self.val(r) and self.val(i) < self.val(l):
                self.swap(i, l)
                self.sift_down(l)
            elif self.val(l) <= self.val(r) and self.val(i) < self.val(r):
                self.swap(i, r)
                self.sift_down(r)
        elif l < size:
            if self.val(i) < self.val(l):
                self.swap(i, l)
                self.sift_down(l)
