from find_all_duplicates_in_an_array import Solution


def test1():
    assert Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test2():
    assert Solution().findDuplicates([1, 1, 2]) == [1]


def test3():
    assert Solution().findDuplicates([1]) == []


def test4():
    assert Solution().findDuplicates([5, 4, 6, 7, 9, 3, 10, 9, 5, 6]) == [9, 5, 6]
