from binary_tree_inorder_traversal import Solution, TreeNode

def test1():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c

    assert Solution().inorderTraversal(a) == [1,3,2]