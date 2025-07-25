from letter_combinations_of_a_phone_number_attempt2 import Solution


def test1():
    assert Solution().letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]


def test2():
    assert Solution().letterCombinations("") == []


def test3():
    assert Solution().letterCombinations("2") == ["a", "b", "c"]
