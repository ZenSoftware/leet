from find_all_numbers_disappeared_in_an_array import Solution


def test1():
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


def test2():
    assert Solution().findDisappearedNumbers([1, 1]) == [2]
