from valid_anagram import Solution

def test1():
    assert Solution().isAnagram('anagram', 'nagaram') == True

def test2():
    assert Solution().isAnagram('rat', 'car') == False