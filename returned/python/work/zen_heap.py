from typing import List

class MinHeap:
    def __init__(self, elements: List = [], key=lambda x: x):
        self.heap = elements
        self.key = key
        self.heapify()

    def __len__(self):
        return len(self.heap)

    def heapify(self):
        for i in reversed(range(len(self.heap))):
            self.sift_down(i)

    def sift_up(self, i: int):
        def val(x):
            return self.key(self.heap[x])
        
        while i != 0 and val(i) < val(p := self.parent_index(i)):
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p
        return i

    def sift_down(self, i: int):
        def val(x):
            return self.key(self.heap[x])
        
        def swap(a,b):
            self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

        size = len(self.heap)
        l = self.left_index(i)
        r = self.right_index(i)
        if l < size and r < size:
            if val(l) < val(r) and val(i) > val(l):
                swap(i, l)
                return self.sift_down(l)
            elif val(l) >= val(r) and val(i) > val(r):
                swap(i, r)
                return self.sift_down(r)
        elif l < size:
            if val(i) > val(l):
                swap(i, l)
                return self.sift_down(l)
        return i

    def push(self, val):
        self.heap.append(val)
        self.sift_up(len(self.heap)-1)

    def peek(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def pop(self):
        if not self.heap:
            return None
        last_index = len(self.heap)-1
        self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
        result = self.heap.pop()
        self.sift_down(0)
        return result
    
    def parent_index(self, i: int) -> int:
        return (i-1)//2

    def left_index(self, i: int) -> int:
        return 2*i+1

    def right_index(self, i: int) -> int:
        return 2*i+2

class MaxHeap(MinHeap):
    def sift_up(self, i: int):
        def val(x):
            return self.key(self.heap[x])
        
        while i != 0 and val(i) > val(p := self.parent_index(i)):
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p
        return i

    def sift_down(self, i: int):
        def val(x):
            return self.key(self.heap[x])
        
        def swap(a,b):
            self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

        size = len(self.heap)
        l = self.left_index(i)
        r = self.right_index(i)
        if l < size and r < size:
            if val(l) > val(r) and val(i) < val(l):
                swap(i, l)
                return self.sift_down(l)
            elif val(l) <= val(r) and val(i) < val(r):
                swap(i, r)
                return self.sift_down(r)
        elif l < size:
            if val(i) < val(l):
                swap(i, l)
                return self.sift_down(l)
        return i