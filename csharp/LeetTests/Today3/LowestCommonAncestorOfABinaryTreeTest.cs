using Today3.LowestCommonAncestorOfABinaryTree;
namespace Today3;

internal class LowestCommonAncestorOfABinaryTreeTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var n3 = new TreeNode(3);
        var n5 = new TreeNode(5);
        var n1 = new TreeNode(1);
        var n6 = new TreeNode(6);
        var n2 = new TreeNode(2);
        var n0 = new TreeNode(0);
        var n8 = new TreeNode(8);
        var n7 = new TreeNode(7);
        var n4 = new TreeNode(4);
        n3.left = n5;
        n3.right = n1;
        n5.left = n6;
        n5.right = n2;
        n1.left = n0;
        n1.right = n8;
        n2.left = n7;
        n2.right = n4;
        var result = solution.LowestCommonAncestor(n3, n5, n1);
        Assert.That(result, Is.EqualTo(n3));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var n3 = new TreeNode(3);
        var n5 = new TreeNode(5);
        var n1 = new TreeNode(1);
        var n6 = new TreeNode(6);
        var n2 = new TreeNode(2);
        var n0 = new TreeNode(0);
        var n8 = new TreeNode(8);
        var n7 = new TreeNode(7);
        var n4 = new TreeNode(4);
        n3.left = n5;
        n3.right = n1;
        n5.left = n6;
        n5.right = n2;
        n1.left = n0;
        n1.right = n8;
        n2.left = n7;
        n2.right = n4;
        var result = solution.LowestCommonAncestor(n3, n5, n4);
        Assert.That(result, Is.EqualTo(n5));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var n1 = new TreeNode(1);
        var n2 = new TreeNode(2);
        n1.left = n2;
        var result = solution.LowestCommonAncestor(n1, n1, n2);
        Assert.That(result, Is.EqualTo(n1));
    }
}