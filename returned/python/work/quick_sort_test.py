from random import randint
from quick_sort import quick_sort

def test1():
    assert quick_sort([5,2,1,4,3]) == [1,2,3,4,5]

def test2():
    original = [randint(1,100) for _ in range(100)]
    input = original.copy()
    quick_sort(input)
    for i in range(1, len(input)):
        assert input[i-1] <= input[i]