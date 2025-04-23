using Today3.ConstructBinaryTreeFromPreorderAndInorderTraversal;
namespace Today3;

internal class ConstructBinaryTreeFromPreorderAndInorderTraversalTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var n3 = new TreeNode(3);
        var n9 = new TreeNode(9);
        var n20 = new TreeNode(20);
        var n15 = new TreeNode(15);
        var n7 = new TreeNode(7);
        n3.left = n9;
        n3.right = n20;
        n20.left = n15;
        n20.right = n7;

        int[] preorder = [3, 9, 20, 15, 7];
        int[] inorder = [9, 3, 15, 20, 7];
        var result = solution.BuildTree(preorder, inorder);
        Assert.That(IsSameTree(result, n3), Is.EqualTo(true));
    }

    private bool IsSameTree(TreeNode a, TreeNode b)
    {
        if (a == null && b == null)
            return true;
        if (a == null || b == null)
            return false;
        return IsSameTree(a.left, b.left) && IsSameTree(a.right, b.right);
    }
}