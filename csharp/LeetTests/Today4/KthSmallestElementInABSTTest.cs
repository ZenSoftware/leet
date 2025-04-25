using Today4.KthSmallestElementInABST;
namespace Today4;

internal class KthSmallestElementInABSTTest
{
    [Test]
    public void Test1()
    {
        var solution = new Solution();
        var n3 = new TreeNode(3);
        var n1 = new TreeNode(1);
        var n4 = new TreeNode(4);
        var n2 = new TreeNode(2);
        n3.left = n1;
        n3.right = n4;
        n1.right = n2;
        var result = solution.KthSmallest(n3, 1);
        Assert.That(result, Is.EqualTo(1));
    }
}