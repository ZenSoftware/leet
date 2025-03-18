from reconstruct_original_digits_from_english import Solution

def test1():
    assert Solution().originalDigits('owoztneoer') == '012'

def test2():
    assert Solution().originalDigits('fviefuro') == '45'
