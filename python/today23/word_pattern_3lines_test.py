from word_pattern_3lines import Solution

def test1():
    assert Solution().wordPattern('abba', 'dog cat cat dog') == True

def test2():
    assert Solution().wordPattern('abba', 'dog cat cat fish') == False

def test3():
    assert Solution().wordPattern('aaaa', 'dog cat cat dog') == False