from quick_select import kth_largest
from random import shuffle

def test1():
    MAX = 100
    input = [i for i in range(1, MAX+1)]
    shuffle(input)
    for i in range(1, MAX+1):
        answer = MAX - i + 1
        assert kth_largest(input, i) == answer