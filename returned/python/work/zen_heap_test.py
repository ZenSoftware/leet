from zen_heap import MinHeap
from random import randint

def test1():
    heap = MinHeap([randint(1,100) for _ in range(100)])
    sorted = []
    while len(heap):
        sorted.append(heap.pop())
    for i in range(1, len(sorted)):
        assert sorted[i-1] <= sorted[i]

def test_push():
    heap = MinHeap()
    for i in range(100):
        heap.push(randint(1,100))
    sorted = []
    while len(heap):
        sorted.append(heap.pop())
    for i in range(1, len(sorted)):
        assert sorted[i-1] <= sorted[i]

def test_sift_down():
    heap = MinHeap()
    heap.heap = [3,2,1]
    heap.sift_down(0)
    assert heap.heap == [1,2,3]