from typing import List


class MinHeap:
    def __init__(self, elements: List = [], key=None):
        self.heap = elements
        self.key = key
        self.heapify()

    def __len__(self):
        return len(self.heap)

    def heapify(self):
        for i in reversed(range(len(self.heap))):
            self.sift_down(i)

    def sift_up(self, i: int):
        if self.key is None:
            while i != 0 and self.heap[i] < self.heap[p := (i - 1) // 2]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
        else:
            while i != 0 and self.key(self.heap[i]) < self.key(
                self.heap[p := (i - 1) // 2]
            ):
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p

    def sift_down(self, i: int):
        def sift_down_with_key(i: int):
            size = len(self.heap)
            l = 2 * i + 1
            r = 2 * i + 2
            if l < size and r < size:
                if self.key(self.heap[l]) < self.key(self.heap[r]) and self.key(
                    self.heap[i]
                ) > self.key(self.heap[l]):
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_with_key(l)
                elif self.key(self.heap[l]) >= self.key(self.heap[r]) and self.key(
                    self.heap[i]
                ) > self.key(self.heap[r]):
                    self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
                    sift_down_with_key(r)
            elif l < size:
                if self.key(self.heap[i]) > self.key(self.heap[l]):
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_with_key(l)

        def sift_down_without_key(i: int):
            size = len(self.heap)
            l = 2 * i + 1
            r = 2 * i + 2
            if l < size and r < size:
                if self.heap[l] < self.heap[r] and self.heap[i] > self.heap[l]:
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_without_key(l)
                elif self.heap[l] >= self.heap[r] and self.heap[i] > self.heap[r]:
                    self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
                    sift_down_without_key(r)
            elif l < size:
                if self.heap[i] > self.heap[l]:
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_without_key(l)

        if self.key is None:
            sift_down_without_key(i)
        else:
            sift_down_with_key(i)

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
        if self.key is None:
            while i != 0 and self.heap[i] > self.heap[p := (i - 1) // 2]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
        else:
            while i != 0 and self.key(self.heap[i]) > self.key(
                self.heap[p := (i - 1) // 2]
            ):
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p

    def sift_down(self, i: int):
        def sift_down_with_key(i: int):
            size = len(self.heap)
            l = 2 * i + 1
            r = 2 * i + 2
            if l < size and r < size:
                if self.key(self.heap[l]) > self.key(self.heap[r]) and self.key(
                    self.heap[i]
                ) < self.key(self.heap[l]):
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_with_key(l)
                elif self.key(self.heap[l]) <= self.key(self.heap[r]) and self.key(
                    self.heap[i]
                ) < self.key(self.heap[r]):
                    self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
                    sift_down_with_key(r)
            elif l < size:
                if self.key(self.heap[i]) < self.key(self.heap[l]):
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_with_key(l)

        def sift_down_without_key(i: int):
            size = len(self.heap)
            l = 2 * i + 1
            r = 2 * i + 2
            if l < size and r < size:
                if self.heap[l] > self.heap[r] and self.heap[i] < self.heap[l]:
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_without_key(l)
                elif self.heap[l] <= self.heap[r] and self.heap[i] < self.heap[r]:
                    self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
                    sift_down_without_key(r)
            elif l < size:
                if self.heap[i] < self.heap[l]:
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    sift_down_without_key(l)

        if self.key is None:
            sift_down_without_key(i)
        else:
            sift_down_with_key(i)
