using Today3.SubtreeOfAnotherTree;
namespace Today3;

internal class SubtreeOfAnotherTreeTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();

        var a3 = new TreeNode(3);
        var a4 = new TreeNode(4);
        var a5 = new TreeNode(5);
        var a1 = new TreeNode(1);
        var a2 = new TreeNode(2);
        a3.left = a4;
        a3.right = a5;
        a4.left = a1;
        a4.right = a2;

        var b4 = new TreeNode(4);
        var b1 = new TreeNode(1);
        var b2 = new TreeNode(2);
        b4.left = b1;
        b4.right = b2;

        var result = solution.IsSubtree(a3, b4);
        Assert.That(result, Is.EqualTo(true));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();

        var a3 = new TreeNode(3);
        var a4 = new TreeNode(4);
        var a5 = new TreeNode(5);
        var a1 = new TreeNode(1);
        var a2 = new TreeNode(2);
        var a0 = new TreeNode(0);
        a3.left = a4;
        a3.right = a5;
        a4.left = a1;
        a4.right = a2;
        a2.left = a0;

        var b4 = new TreeNode(4);
        var b1 = new TreeNode(1);
        var b2 = new TreeNode(2);
        b4.left = b1;
        b4.right = b2;

        var result = solution.IsSubtree(a3, b4);
        Assert.That(result, Is.EqualTo(false));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();

        var a1 = new TreeNode(1);
        var a11 = new TreeNode(1);
        a1.left = a11;

        var b1 = new TreeNode(1);

        var result = solution.IsSubtree(a1, b1);
        Assert.That(result, Is.EqualTo(true));
    }
}