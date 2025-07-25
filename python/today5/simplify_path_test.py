from simplify_path import Solution

def test1():
    assert Solution().simplifyPath("/home/") == "/home"

def test2():
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"

def test3():
    assert Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"

def test4():
    assert Solution().simplifyPath("/../") == "/"
    
def test5():
    assert Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
