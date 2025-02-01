from binary_search import binary_search

def test1():
    input = [0,1,2,3,4,5,6,7,8,9]
    assert binary_search(input, -1) == -1
    assert binary_search(input, 0) == 0
    assert binary_search(input, 1) == 1
    assert binary_search(input, 2) == 2
    assert binary_search(input, 3) == 3
    assert binary_search(input, 4) == 4
    assert binary_search(input, 5) == 5
    assert binary_search(input, 6) == 6
    assert binary_search(input, 7) == 7
    assert binary_search(input, 8) == 8
    assert binary_search(input, 9) == 9
    assert binary_search(input, 10) == -1