from house_robber_iii import Solution, TreeNode

def test1():
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(3)
    e = TreeNode(1)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    assert Solution().rob(a) == 7

def test2():
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(5)
    d = TreeNode(1)
    e = TreeNode(3)
    f = TreeNode(1)
    a.left = b
    a.right =c
    b.left = d
    b.right = e
    c.right = f
    assert Solution().rob(a) == 9