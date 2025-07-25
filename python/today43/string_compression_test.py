from string_compression import Solution


def test1():
    arr = ["a", "a", "b", "b", "c", "c", "c"]
    assert Solution().compress(arr) == 6
    assert arr == ["a", "2", "b", "2", "c", "3", "c"]


def test2():
    arr = ["a"]
    assert Solution().compress(arr) == 1
    assert arr == ["a"]


def test3():
    arr = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert Solution().compress(arr) == 4
    assert arr == ["a", "b", "1", "2", "b", "b", "b", "b", "b", "b", "b", "b", "b"]


def test4():
    arr = ["a", "b", "c"]
    assert Solution().compress(arr) == 3
    assert arr == ["a", "b", "c"]


def test5():
    arr = ["a", "a", "a", "a", "a", "b"]
    assert Solution().compress(arr) == 3
    assert arr == ["a", "5", "b", "a", "a", "b"]
