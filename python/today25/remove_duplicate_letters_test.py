from remove_duplicate_letters import Solution

def test1():
    assert Solution().removeDuplicateLetters('bcabc') == 'abc'

def test2():
    assert Solution().removeDuplicateLetters('cbacdcbc') == 'acdb'