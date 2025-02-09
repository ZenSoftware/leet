from validate_binary_search_tree import Solution, TreeNode

def test1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    b.left = a
    b.right = c
    assert Solution().isValidBST(b) == True

def test2():
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n6 = TreeNode(6)
    n3 = TreeNode(3)
    n7 = TreeNode(7)
    n5.left = n4
    n5.right = n6
    n6.left = n3
    n6.right = n7

    assert Solution().allGreaterThan(n5, n6) == False
    assert Solution().isValidBST(n5) == False
