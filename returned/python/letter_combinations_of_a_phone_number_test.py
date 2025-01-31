from letter_combinations_of_a_phone_number import Solution

def test1():
    assert Solution.letterCombinations(None, "23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test2():
    assert Solution.letterCombinations(None, "") == []

def test3():
    assert Solution.letterCombinations(None, "2") == ["a","b","c"]