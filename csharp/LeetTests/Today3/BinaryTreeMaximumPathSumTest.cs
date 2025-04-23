using Today3.BinaryTreeMaximumPathSum;
using Leet.Tree;
namespace Today3;

internal class BinaryTreeMaximumPathSumTest()
{
    [Test]
    public void Test1()
    {
        var n1 = new TreeNode(1);
        var n2 = new TreeNode(2);
        var n3 = new TreeNode(3);
        n1.left = n2;
        n1.right = n3;
        var solution = new Solution();
        var result = solution.MaxPathSum(n1);
        Assert.That(result, Is.EqualTo(6));
    }

    [Test]
    public void Test2()
    {
        var n10 = new TreeNode(-10);
        var n9 = new TreeNode(9);
        var n20 = new TreeNode(20);
        var n15 = new TreeNode(15);
        var n7 = new TreeNode(7);
        n10.left = n9;
        n10.right = n20;
        n20.left = n15;
        n20.right = n7;
        var solution = new Solution();
        var result = solution.MaxPathSum(n10);
        Assert.That(result, Is.EqualTo(42));
    }

    [Test]
    public void Test3()
    {
        var n2 = new TreeNode(-2);
        var n1 = new TreeNode(1);
        n2.left = n1;
        var solution = new Solution();
        var result = solution.MaxPathSum(n2);
        Assert.That(result, Is.EqualTo(1));
    }
}