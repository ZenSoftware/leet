using Today3.BinaryTreeRightSideView;
namespace Today3;

internal class BinaryTreeRightSideViewTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var n1 = new TreeNode(1);
        var n2 = new TreeNode(2);
        var n3 = new TreeNode(3);
        var n4 = new TreeNode(4);
        var n5 = new TreeNode(5);
        n1.left = n2;
        n1.right = n3;
        n2.right = n5;
        n3.right = n4;
        var result = solution.RightSideView(n1);
        Assert.That(result, Is.EqualTo([1, 3, 4]));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var n1 = new TreeNode(1);
        var n2 = new TreeNode(2);
        var n3 = new TreeNode(3);
        var n4 = new TreeNode(4);
        var n5 = new TreeNode(5);
        n1.left = n2;
        n1.right = n3;
        n2.left = n4;
        n4.left = n5;
        var result = solution.RightSideView(n1);
        Assert.That(result, Is.EqualTo([1, 3, 4, 5]));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var n1 = new TreeNode(1);
        var n3 = new TreeNode(3);
        n1.right = n3;
        var result = solution.RightSideView(n1);
        Assert.That(result, Is.EqualTo([1, 3]));
    }

    [Test]
    public void Test4()
    {
        var solution = new Solution();
        var result = solution.RightSideView(null);
        Assert.That(result, Is.Empty);
    }
}