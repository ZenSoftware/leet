from longest_repeating_character_replacement import Solution

def test1():
    assert Solution().characterReplacement('ABAB', 2) == 4

def test2():
    assert Solution().characterReplacement('AABABBA', 1) == 4

def test3():
    assert Solution().characterReplacement('AAAA', 0) == 4

def test4():
    assert Solution().characterReplacement('BAAAA', 0) == 4

def test5():
    assert Solution().characterReplacement('AAABBAAAA', 1) == 5