from contains_duplicate_attempt2 import Solution


def test1():
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True


def test2():
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False


def test3():
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
