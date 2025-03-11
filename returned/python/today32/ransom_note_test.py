from ransom_note import Solution

def test1():
    assert Solution().canConstruct('a', 'b') == False
    assert Solution().canConstruct('aa', 'ab') == False
    assert Solution().canConstruct('aa', 'aab') == True