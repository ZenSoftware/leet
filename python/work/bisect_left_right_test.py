from bisect_left_right import (
    bisect_left as my_bisect_left,
    bisect_right as my_bisect_right,
)
from bisect import bisect_left, bisect_right


def test_bisect_left():
    elements = [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5]
    assert my_bisect_left(elements, 3) == 3
    assert my_bisect_left(elements, 0) == 0
    assert my_bisect_left(elements, 5) == 11
    assert my_bisect_left(elements, 6) == 12
    assert my_bisect_left(elements, -99) == 0

    assert bisect_left(elements, 3) == 3
    assert bisect_left(elements, 0) == 0
    assert bisect_left(elements, 5) == 11
    assert bisect_left(elements, 6) == 12
    assert bisect_left(elements, -99) == 0


def test_bisect_right():
    elements = [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 5]
    assert my_bisect_right(elements, 3) == 10
    assert my_bisect_right(elements, 0) == 1
    assert my_bisect_right(elements, 5) == 12
    assert my_bisect_right(elements, 6) == 12
    assert my_bisect_right(elements, -99) == 0

    assert bisect_right(elements, 3) == 10
    assert bisect_right(elements, 0) == 1
    assert bisect_right(elements, 5) == 12
    assert bisect_right(elements, 6) == 12
    assert bisect_right(elements, -99) == 0
