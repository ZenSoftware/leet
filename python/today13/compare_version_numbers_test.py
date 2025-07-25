from compare_version_numbers import Solution

def test1():
    assert Solution().compareVersion("1.2", "1.10") == -1
    
def test2():
    assert Solution().compareVersion("1.01", "1.001") == 0

def test3():
    assert Solution().compareVersion("1.0", "1.0.0.0") == 0
