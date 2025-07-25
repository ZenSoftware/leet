from binary_tree_right_side_view import Solution, TreeNode

def test1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n4.left = n5
    
    result = Solution().rightSideView(n1)
    assert result == [1,3,4,5]