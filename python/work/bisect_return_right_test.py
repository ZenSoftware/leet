from bisect_return_right import bisect_return_right


def test1():
    arr = [0, 1, 2, 3, 4, 5]
    assert bisect_return_right(arr, -1) == -1
    assert bisect_return_right(arr, 0) == 0
    assert bisect_return_right(arr, 1) == 1
    assert bisect_return_right(arr, 2) == 2
    assert bisect_return_right(arr, 3) == 3
    assert bisect_return_right(arr, 4) == 4
    assert bisect_return_right(arr, 5) == 5
    assert bisect_return_right(arr, 6) == 5

    arr = [0, 1, 2, 3, 4]
    assert bisect_return_right(arr, -1) == -1
    assert bisect_return_right(arr, 0) == 0
    assert bisect_return_right(arr, 1) == 1
    assert bisect_return_right(arr, 2) == 2
    assert bisect_return_right(arr, 3) == 3
    assert bisect_return_right(arr, 4) == 4
    assert bisect_return_right(arr, 5) == 4
