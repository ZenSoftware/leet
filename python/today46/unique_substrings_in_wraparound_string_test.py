from unique_substrings_in_wraparound_string import Solution


def test1():
    assert Solution().findSubstringInWraproundString("a") == 1


def test2():
    assert Solution().findSubstringInWraproundString("cac") == 2


def test3():
    assert Solution().findSubstringInWraproundString("zab") == 6


def test4():
    assert Solution().findSubstringInWraproundString("aabb") == 3
