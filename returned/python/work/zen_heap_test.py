from zen_heap import MinHeap, MaxHeap
from random import randint
from heapq import heapify, heappush

def test_min_heap():
    heap = MinHeap([randint(1,100) for _ in range(100)])
    sorted = []
    while len(heap):
        sorted.append(heap.pop())
    for i in range(1, len(sorted)):
        assert sorted[i-1] <= sorted[i]

def test_max_heap():
    heap = MaxHeap([randint(1,100) for _ in range(100)])
    sorted = []
    while len(heap):
        sorted.append(heap.pop())
    for i in range(1, len(sorted)):
        assert sorted[i-1] >= sorted[i]

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

def test_heapq_heapify_equivalency():
    input_mine = [randint(1,100) for _ in range(100)]
    input_heapq = input_mine.copy()
    my_heap = MinHeap(input_mine)
    heapify(input_heapq)
    assert input_heapq == my_heap.heap

def test_heapq_push_equivalency():
    input = [randint(1,100) for _ in range(100)]
    my_heap = MinHeap()
    heapq_heap = []
    for el in input:
        my_heap.push(el)
        heappush(heapq_heap, el)
    assert my_heap.heap == heapq_heap