from add_strings import Solution

def test1():
    assert Solution().addStrings('11', '123') == '134'
    assert Solution().addStrings('456', '77') == '533'
    assert Solution().addStrings('0', '0') == '0'