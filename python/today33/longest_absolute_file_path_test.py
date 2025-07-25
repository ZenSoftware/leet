from longest_absolute_file_path import Solution

def test1():
    assert Solution().lengthLongestPath('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext') == 20

def test2():
    assert Solution().lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext') == 32

def test3():
    assert Solution().lengthLongestPath('a') == 0