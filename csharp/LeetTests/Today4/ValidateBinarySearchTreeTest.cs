using Today4.ValidateBinarySearchTree;
namespace Today4;

internal class ValidateBinarySearchTreeTest()
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var n2 = new TreeNode(2);
        var n1 = new TreeNode(1);
        var n3 = new TreeNode(3);
        n2.left = n1;
        n2.right = n3;
        var result = solution.IsValidBST(n2);
        Assert.That(result, Is.EqualTo(true));
    }

    [Test]
    public void Test2()
    {
        var solution = new Solution();
        var n5 = new TreeNode(5);
        var n1 = new TreeNode(1);
        var n4 = new TreeNode(4);
        var n3 = new TreeNode(3);
        var n6 = new TreeNode(6);
        n5.left = n1;
        n5.right = n4;
        n4.left = n3;
        n4.right = n6;
        var result = solution.IsValidBST(n5);
        Assert.That(result, Is.EqualTo(false));
    }

    [Test]
    public void Test3()
    {
        var solution = new Solution();
        var n5 = new TreeNode(5);
        var n4 = new TreeNode(4);
        var n6 = new TreeNode(6);
        var n3 = new TreeNode(3);
        var n7 = new TreeNode(7);
        n5.left = n4;
        n5.right = n6;
        n6.left = n3;
        n6.right = n7;
        var result = solution.IsValidBST(n5);
        Assert.That(result, Is.EqualTo(false));
    }

    [Test]
    public void Test4()
    {
        var solution = new Solution();
        var n = new TreeNode(2_147_483_647);
        var result = solution.IsValidBST(n);
        Assert.That(result, Is.EqualTo(true));
    }
}