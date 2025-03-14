from decode_string import Solution

def test1():
    assert Solution().decodeString('3[a]2[bc]') == 'aaabcbc'

def test2():
    assert Solution().decodeString('3[a2[c]]') == 'accaccacc'

def test3():
    assert Solution().decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'