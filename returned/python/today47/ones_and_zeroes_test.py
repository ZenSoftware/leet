from ones_and_zeroes import Solution


def test1():
    strs = ["10", "0001", "111001", "1", "0"]
    assert Solution().findMaxForm(strs, 5, 3) == 4


def test2():
    strs = ["10", "0", "1"]
    assert Solution().findMaxForm(strs, 1, 1) == 2


def test3():
    strs = [
        "101000000",
        "1100001010",
        "11101000",
        "011010110",
        "0010001",
        "0011",
        "0111101111",
    ]
    assert Solution().findMaxForm(strs, 10, 11) == 3


def test4():
    strs = ["00", "01", "01"]
    assert Solution().findMaxForm(strs, 2, 2) == 2
